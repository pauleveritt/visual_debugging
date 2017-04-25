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



### Old-Fashioned Debugging

- Problem: Where is 0,0
- print statements
- import pdb; pdb.set_trace()


### Visual Debugging

- Run program like normal, under the debugger
- Install Cython speedups
- Use breakpoint to solve first problem

### Poking Around

- Problem: I want to use f-string `f'Score: {self.score:02d}'` but I'm not sure how
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
- Problem: How does Arcade collisions work?
- Add code then step into

### Watch Expressions

- Problem: Are the number of coins actually decreasing?
- Set breakpoint in for coin in hit_list
- Add a watch expression: len(self.coin_list)
- Cause collision with multiple coins
- Step through and see the watch expression value

### Stack Frames

- Problem: Which coin is in _set_center_x?
- In for loop, step into setting the x
- Move back up the stack
- Observe the watch expression and self.score

### Debug During Testing

- Problem: TDD for "Don't show score when mouse is moving"

- Write a test to see if score goes up on collision

- It fails, I'm confused

- Use debugging

- Fix tests, clear breakpoint, re-run

### Attach to Process

- Run ``game.py`` from command line

- Use "Attach to Process" and then debug it

### Extract Type Information

- Preferences -> Build -> Python Debugger, checkbox for 
  `Collect`

### Django and Flask 

- Open Flask project

- Set a breakpoint in a template

### Extra Credit

- NodeJS/Chrome debugging

- Configuring Stepping 

- Keyboard shortcuts for stepping

- Show Execution Point button in toolbar when you get lost

- Mute Breakpoints button

- Inspect watch value in separate window

