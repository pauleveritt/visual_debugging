## Visual Debugging Webinar

Webinar April 25 to show debugging visually.

- Debugging without PyCharm's debugger: print and pdb
- First use of the debugger (and the Cython speedups)
- Breakpoints
- Using the console/IPython at a breakpoint
- Conditional breakpoints
- All flavors of stepping through code
- Moving through stack frames
- Setting watches
- Attaching to processes
- Debugging during testing
- Extracting type information
- Django/Flask template debugging
- Viewing numpy/pandas data frames

### Before

- Delete Cython speedups
  * <your distribution>\helpers\pydev\_pydevd_bundle
  * Remove pydevd_cython.so
- Uninstall ipython
- Default theme, big font
- Turn off Notifications and other toolbar stuff
- Ensure Presentation Assistant is on
- 1280x720
- Check value of break on any Python exception
- Django/Flask template debugging projects open
- Test exists, with a run configuration for all tests
- Have the numpy/pandas project open

### Old-Fashioned Debugging

- First problem to solve
- print statements
- 
- import pdb; pdb.set_trace()

### Visual Debugging

- Run program like normal, under the debugger
- Install Cython speedups
- Use breakpoint to solve first problem

### Poking Around

- Problem: I want to use f-string but I'm not sure how
- Interactive would help
- Set breakpoint, then use Evaluate Expression
- Or, Console
- Install iPython and use it

### Breakpoints

- Problem: What is that "delta_time" thing?
- Set breakpoint, observe value, click "Continue"
- Clear breakpoint, click "Continue"
- Problem: wrong filename, what directory am I in?
- Any Exception breakpoint

## Stepping

- Problem: 50 coins at random positions
- Add for loop, but is random doing the right thing?
- Set breakpoint, start regular stepping
- Set breakpoint outside, and step into
- Ditto, step over
- Run to cursor
- Problem: How does Arcade collisions work?
- Add code then step into

### Watch Expressions

- Problem: Are the number of coins actually decreasing?
- Set breakpoint in for coin in hit_list
- Add a watch expressin: len(self.coin_list)
- Cause collision with multiple coins
- Step through and see the watch expression value

### Stack Frames

- Problem: Refactor the collision code to handle "model" 
  of (a) get rid of sprite and (b) increase score
- Change code
- Set breakpoint after score is increased and coin removed
- Move back up the stack
- Observe the watch expression and self.score

### Debug During Testing

- Problem: My "score is increasing" test doesn't match the 
  value that I'm expecting

- Write a test to see if score goes up on collision

- It fails, I'm confused

- Use debugging

- Fix tests, clear breakpoint, re-run

### Attach to Process

### Extract Type Information

### Django and Flask 