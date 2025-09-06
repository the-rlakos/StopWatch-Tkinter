import tkinter as tk, time

class StopwatchApp:
    def __init__(self, root):
        self.root=root; self.root.title("Stopwatch"); self.root.geometry("260x160")
        self.start_time=None; self.running=False; self.elapsed=0.0
        self.label=tk.Label(root,text="00:00.00",font=("Helvetica",32))
        self.label.pack(pady=10)
        # buttons
        b=tk.Frame(root); b.pack()
        tk.Button(b,text="Start",command=self.start).grid(row=0,column=0,padx=5)
        tk.Button(b,text="Stop",command=self.stop).grid(row=0,column=1,padx=5)
        tk.Button(b,text="Reset",command=self.reset).grid(row=0,column=2,padx=5)
        self.update_ui()

    def format_time(self,s):
        m=int(s//60); sec=int(s%60); cs=int((s-int(s))*100)
        return f"{m:02d}:{sec:02d}.{cs:02d}"

    def update_ui(self):
        if self.running: self.elapsed=time.time()-self.start_time
        self.label.config(text=self.format_time(self.elapsed))
        self.root.after(10,self.update_ui)

    def start(self):
        if not self.running:
            self.start_time=time.time()-self.elapsed; self.running=True
    def stop(self): self.running=False
    def reset(self): self.running=False; self.elapsed=0.0

if __name__=="__main__":
    root=tk.Tk(); app=StopwatchApp(root); root.mainloop()
