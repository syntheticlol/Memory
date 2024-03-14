import ctypes, sys, gc

class memory:
    def __init__(self):
        if sys.platform.startswith('win'):
            self.pydll = "python38.dll"
        else:  # you need to choose your version 3.8 is mine :)))
            self.pydll = "libpython3.8.so"
        
        self.pd = ctypes.PyDLL(self.pydll)
        self.PyMem_RawFree = self.pd.PyMem_RawFree
        self.PyMem_RawFree.argtypes = [ctypes.c_void_p]

    def allocatemem(self, size):
        return ctypes.create_string_buffer(size)

    def thisisfax(self):
        something = self.allocatemem(1024 * 1024 * 10)
        self.PyMem_RawFree(ctypes.addressof(something))
        gc.collect()
        print("Done..")

if __name__ == "__main__":
    iguess = memory()
    iguess.thisisfax()
