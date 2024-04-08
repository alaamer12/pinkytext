# About
this project just try to make animated colored text, it may be extended to provide coloring functionally

# Pinkytext

it provides colors and gradient text for your terminal

## Install

```bash
pip install pinkytext
```

## Usage

``` python
import pinkytext

pinkytext.flicker_text("Hello, World!", [(255, 0, 0), (0, 255, 0), (0, 0, 255)])

pinkytext.wave("Hello, World!", "Hello, World!", 0.009)

pinkytext.wave_gradient_text("Hello, World!", [(255, 0, 0), (0, 255, 0), (0, 0, 255)])

pinkytext.gradient_text("Hello, World!", [(255, 0, 0), (0, 255, 0), (0, 0, 255)])

pinkytext.Animation().wave("Hello, World!", "Hello, World!", 0.009)

pinkytext.Animation().wave_gradient_text("Hello, World!", [(255, 0, 0), (0, 255, 0), (0, 0, 255)])
```


