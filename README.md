## Repo

### `https://githubcom/pauleveritt/visual_debugging`

## Visual Debugging Webinar

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

### Setup

- Darcula, big font
- Tab-less, clutter-free
- View -> Description of Actions

### Old-Fashioned Debugging

- Problem: Where is 0,0
- print statements in on_mouse_motion
- import pdb; pdb.set_trace()
- `p x` and `p y`


### Visual Debugging

- Run program like normal, under the debugger
- Use breakpoint to solve first problem

### Poking Around

- Problem: I want to use f-string `f'Score: {self.score:02d}'` but I'm not sure how
- Interactive would help
- Set breakpoint
- Use the inline comment values to see variables
- Use Evaluate Expression
- Or, Console
- Install ipython and use it

### Breakpoints

- Problem: What is that "delta_time" thing?
- Set breakpoint, observe value, click "Continue", check again
- Clear breakpoint, click "Continue"
- Resume
- Set a different breakpoint without restarting
- Problem: typo in filename, what directory am I in?
- Any Exception breakpoint
- Explain  "Frames" to see what called it
- Conditional Breakpoint: Score > 9 (in double digits)

## Stepping

- Problem: 50 coins at random positions
- Stepping 1: for loop, but is random doing the right thing?
- Set breakpoint, start regular stepping
- Set breakpoint outside, and step into
- Step *into* `arcade.Sprite` constructor, then step out
- Ditto, step over
- Step accidentally into random, show Step Into My Code
- Run to Cursor
- Problem: How does Arcade collisions work?
- Stepping 2
- Add code then step into

### Watch Expressions

- Problem: Are the number of coins actually decreasing?
- Set breakpoint in for coin in hit_list and stop there
- Ugh, lots of things to scroll through
- Add a watch expression: len(self.coin_list)
- Cause collision with multiple coins
- Step through and see the watch expression value

### Stack Frames

- Problem: Which coin is in _set_center_x?
- Set breakpoint after "Stack Frames"
- In for loop, step into setting the x
- Reveals that `center_x` is actually a *property*, not an attribute
- Move back up the stack to see which coin we're on `i`
- Observe the watch expression and self.score

### Debug During Testing

- Problem: TDD for "Don't show score when mouse is moving"
- Write a test to see if score goes up on collision
- First, go into "TDD Mode", open `test_mygame`
- It fails, I'm confused
- Use debugging
- Fix tests, clear breakpoint, re-run

### Attach to Process

- Run ``game.py`` from command line
- Use "Attach to Process" and then debug it

### Extract Type Information

- Preferences -> Build -> Python Debugger, checkbox for  `Collect`
- Run game under debugger, move around
- Alt-Enter on `__init__`

### Django and Flask 

- Wouldn't it be nice to do breakpoints in...templates?!
- Open Django project
- Set a breakpoint in a template
