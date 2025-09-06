# Stopwatch-Tkinter

A minimal **stopwatch** with **Start**, **Stop**, and **Reset** built with Tkinter.

## How it Works
1. The app keeps track of `start_time`, `elapsed`, and `running`.
2. `update_ui()` is scheduled every 10 ms via `root.after(10, ...)` to refresh the displayed time.
3. **Start** computes a new `start_time` adjusted by any previously elapsed time.
4. **Stop** freezes the elapsed time.
5. **Reset** clears the elapsed time and stops the watch.

## File Structure
```
Stopwatch-Tkinter/
└─ app.py
```

## Run
```bash
python app.py
```

## Next Steps (Optional)
- Add lap times.
- Add keyboard shortcuts (e.g., Space = start/stop).
- Save the last time on exit.
