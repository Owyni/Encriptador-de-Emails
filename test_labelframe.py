import ttkbootstrap as ttk
try:
    print(f"Has LabelFrame: {hasattr(ttk, 'LabelFrame')}")
    print(f"Has Labelframe: {hasattr(ttk, 'Labelframe')}")
except Exception as e:
    print(e)
