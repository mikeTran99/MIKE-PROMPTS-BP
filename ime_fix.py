# -*- coding: utf-8 -*-
"""
IME FIX v3 — Fix triệt để 3 vấn đề:
1. Segfault khi gõ tiếng Việt (block WM_IME_COMPOSITION khỏi Tk)
2. System menu hiện khi gõ Space (block WM_SYSCOMMAND SC_KEYMENU)  
3. Alt key bị kẹt sau IME composition (eat WM_SYSKEYDOWN VK_MENU)

Kỹ thuật: WndProc subclass cho TỪNG widget + top-level window.
- Widget hook: chặn IME messages, tự extract text qua IMM32 API
- Toplevel hook: chặn system menu trigger

Changelog:
- v1: return 0 → text mất vì dùng after_idle
- v2: DefWindowProcW → system menu do Alt state corrupt
- v3: return 0 + direct insert + block Alt + block system menu
"""
import sys
import traceback


def apply_ime_fix(widget, debug=False):
    """Áp dụng IME fix cho tk.Text hoặc tk.Entry widget."""
    if sys.platform != 'win32':
        return
    try:
        _apply_widget_hook(widget, debug)
    except Exception as e:
        _log_error(f"Widget hook failed: {e}")


def apply_toplevel_fix(toplevel_widget, debug=False):
    """Áp dụng system menu fix cho top-level window (CTk/Tk root).
    
    Chặn WM_SYSCOMMAND SC_KEYMENU — ngăn system menu hiện khi Alt bị kẹt.
    """
    if sys.platform != 'win32':
        return
    try:
        _apply_toplevel_hook(toplevel_widget, debug)
    except Exception as e:
        _log_error(f"Toplevel hook failed: {e}")


def _log_error(msg):
    try:
        sys.stderr.write(f"[IME_FIX] {msg}\n")
        sys.stderr.flush()
    except Exception:
        pass


def _apply_widget_hook(widget, debug):
    """Hook WndProc cho input widget — chặn IME crash + Alt stuck."""
    import ctypes
    from ctypes import wintypes
    import tkinter as tk
    
    WM_IME_STARTCOMPOSITION = 0x010D
    WM_IME_ENDCOMPOSITION   = 0x010E
    WM_IME_COMPOSITION      = 0x010F
    WM_IME_NOTIFY           = 0x0282
    WM_SYSKEYDOWN           = 0x0104
    WM_SYSKEYUP             = 0x0105
    GCS_RESULTSTR           = 0x0800
    VK_MENU                 = 0x12   # Alt key
    GWL_WNDPROC             = -4
    
    WNDPROC = ctypes.WINFUNCTYPE(
        ctypes.c_longlong,
        wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM,
    )
    
    user32 = ctypes.windll.user32
    imm32  = ctypes.windll.imm32
    
    user32.CallWindowProcW.restype  = ctypes.c_longlong
    user32.CallWindowProcW.argtypes = [
        ctypes.c_void_p, wintypes.HWND, wintypes.UINT,
        wintypes.WPARAM, wintypes.LPARAM
    ]
    user32.SetWindowLongPtrW.restype  = ctypes.c_void_p
    user32.SetWindowLongPtrW.argtypes = [wintypes.HWND, ctypes.c_int, ctypes.c_void_p]
    user32.GetWindowLongPtrW.restype  = ctypes.c_void_p
    user32.GetWindowLongPtrW.argtypes = [wintypes.HWND, ctypes.c_int]
    
    imm32.ImmGetContext.restype  = wintypes.HANDLE
    imm32.ImmGetContext.argtypes = [wintypes.HWND]
    imm32.ImmReleaseContext.restype  = wintypes.BOOL
    imm32.ImmReleaseContext.argtypes = [wintypes.HWND, wintypes.HANDLE]
    imm32.ImmGetCompositionStringW.restype  = ctypes.c_long
    imm32.ImmGetCompositionStringW.argtypes = [
        wintypes.HANDLE, wintypes.DWORD, ctypes.c_void_p, wintypes.DWORD
    ]
    
    hwnd = widget.winfo_id()
    if not hwnd:
        raise RuntimeError("Widget chưa có HWND")
    
    old_wndproc = user32.GetWindowLongPtrW(hwnd, GWL_WNDPROC)
    if not old_wndproc:
        raise RuntimeError(f"GetWindowLongPtrW failed")
    
    is_text = isinstance(widget, tk.Text)
    
    def _insert(text):
        """Insert text tại cursor — an toàn."""
        try:
            widget.insert(tk.INSERT, text)
        except Exception:
            pass
    
    def _dbg(msg):
        if debug:
            try:
                sys.stderr.write(f"[IME] {msg}\n")
                sys.stderr.flush()
            except Exception:
                pass
    
    @WNDPROC
    def hooked(h, msg, wp, lp):
        try:
            # ── CHẶN IME COMPOSITION — thủ phạm crash ───────
            if msg == WM_IME_COMPOSITION:
                if lp & GCS_RESULTSTR:
                    himc = imm32.ImmGetContext(h)
                    if himc:
                        try:
                            size = imm32.ImmGetCompositionStringW(himc, GCS_RESULTSTR, None, 0)
                            if size > 0:
                                buf = ctypes.create_unicode_buffer(size // 2 + 1)
                                imm32.ImmGetCompositionStringW(himc, GCS_RESULTSTR, buf, size + 2)
                                text = buf.value
                                if text:
                                    _dbg(f"RESULT: '{text}'")
                                    _insert(text)
                        finally:
                            imm32.ImmReleaseContext(h, himc)
                # BLOCK — không cho Tk và cũng không cho DefWindowProc xử lý
                return 0
            
            # ── CHẶN START/END COMPOSITION ───────────────────
            if msg in (WM_IME_STARTCOMPOSITION, WM_IME_ENDCOMPOSITION):
                return 0
            
            # ── CHẶN IME NOTIFY ──────────────────────────────
            if msg == WM_IME_NOTIFY:
                return 0
            
            # ── CHẶN ALT KEY bị kẹt ─────────────────────────
            # IME có thể inject WM_SYSKEYDOWN cho VK_MENU (Alt)
            # Nếu không chặn → Space sau đó = Alt+Space = system menu
            if msg in (WM_SYSKEYDOWN, WM_SYSKEYUP):
                if wp == VK_MENU:
                    _dbg(f"BLOCKED Alt key (msg={hex(msg)})")
                    return 0
            
        except Exception:
            _dbg(f"Hook error: {traceback.format_exc()}")
        
        # Mọi message khác → Tk bình thường
        return user32.CallWindowProcW(old_wndproc, h, msg, wp, lp)
    
    # Giữ reference
    widget._ime_hook = hooked
    widget._ime_old = old_wndproc
    widget._ime_hwnd = hwnd
    
    ptr = ctypes.cast(hooked, ctypes.c_void_p).value
    user32.SetWindowLongPtrW(hwnd, GWL_WNDPROC, ptr)
    _dbg(f"Widget OK — HWND={hwnd:#x}")


def _apply_toplevel_hook(toplevel, debug):
    """Hook WndProc cho top-level window — chặn system menu."""
    import ctypes
    from ctypes import wintypes
    
    WM_SYSCOMMAND = 0x0112
    SC_KEYMENU    = 0xF100   # System menu triggered by Alt
    GWL_WNDPROC   = -4
    
    WNDPROC = ctypes.WINFUNCTYPE(
        ctypes.c_longlong,
        wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM,
    )
    
    user32 = ctypes.windll.user32
    user32.CallWindowProcW.restype  = ctypes.c_longlong
    user32.CallWindowProcW.argtypes = [
        ctypes.c_void_p, wintypes.HWND, wintypes.UINT,
        wintypes.WPARAM, wintypes.LPARAM
    ]
    user32.SetWindowLongPtrW.restype  = ctypes.c_void_p
    user32.SetWindowLongPtrW.argtypes = [wintypes.HWND, ctypes.c_int, ctypes.c_void_p]
    user32.GetWindowLongPtrW.restype  = ctypes.c_void_p
    user32.GetWindowLongPtrW.argtypes = [wintypes.HWND, ctypes.c_int]
    
    # Lấy HWND của top-level window
    # CTk/Tk root.winfo_id() trả về frame HWND, cần HWND thật
    # Dùng GetParent để lên parent cuối cùng
    hwnd = toplevel.winfo_id()
    
    # Tk top-level windows: winfo_id() cho embedded frame
    # Cần lấy parent window (actual Win32 window with system menu)
    user32.GetParent.restype = wintypes.HWND
    user32.GetParent.argtypes = [wintypes.HWND]
    
    parent = user32.GetParent(hwnd)
    while parent:
        hwnd = parent
        parent = user32.GetParent(hwnd)
    
    if not hwnd:
        raise RuntimeError("Cannot find toplevel HWND")
    
    old_wndproc = user32.GetWindowLongPtrW(hwnd, GWL_WNDPROC)
    if not old_wndproc:
        raise RuntimeError(f"GetWindowLongPtrW failed for toplevel")
    
    def _dbg(msg):
        if debug:
            try:
                sys.stderr.write(f"[TOPLEVEL] {msg}\n")
                sys.stderr.flush()
            except Exception:
                pass
    
    @WNDPROC
    def hooked(h, msg, wp, lp):
        try:
            if msg == WM_SYSCOMMAND:
                cmd = wp & 0xFFF0
                if cmd == SC_KEYMENU:
                    _dbg(f"BLOCKED SC_KEYMENU (system menu via Alt)")
                    return 0
        except Exception:
            pass
        
        return user32.CallWindowProcW(old_wndproc, h, msg, wp, lp)
    
    toplevel._ime_toplevel_hook = hooked
    toplevel._ime_toplevel_old = old_wndproc
    toplevel._ime_toplevel_hwnd = hwnd
    
    ptr = ctypes.cast(hooked, ctypes.c_void_p).value
    user32.SetWindowLongPtrW(hwnd, GWL_WNDPROC, ptr)
    _dbg(f"Toplevel OK — HWND={hwnd:#x}")


def remove_ime_fix(widget):
    """Gỡ IME fix."""
    if sys.platform != 'win32':
        return
    try:
        import ctypes
        from ctypes import wintypes
        user32 = ctypes.windll.user32
        user32.SetWindowLongPtrW.argtypes = [wintypes.HWND, ctypes.c_int, ctypes.c_void_p]
        old = getattr(widget, '_ime_old', None)
        hwnd = getattr(widget, '_ime_hwnd', None)
        if old and hwnd:
            user32.SetWindowLongPtrW(hwnd, -4, old)
            widget._ime_hook = None
    except Exception:
        pass
