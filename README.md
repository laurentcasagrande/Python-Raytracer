# Python Raytracer

A small, educational ray tracer written in Python. It builds 3D scenes from geometric primitives, traces rays from a virtual camera, and uses ambient, diffuse, and specular lighting with shadows to render images. The repository also includes two scripts that generate frames for simple animations (like this Horizontally Spinning Rat).

![Horizontally Spinning Rat](Ratte\horizontal_rotierende_Ratte.gif)

## Features

- **3D geometry:** spheres (`Kugel`), planes (`Ebene`), and triangles (`Dreieck`).
- **Lighting and shading:** ambient light, point lights, diffuse shading, specular highlights, and hard shadows.
- **Materials:** configurable RGB colors and ambient, diffuse, and specular coefficients, plus a shininess exponent.
- **Scene animation:** rotation of spheres and triangles about a vertical axis.
- **Image output:** Matplotlib previews and PNG image export.
- **Video export:** an optional utility that converts a sequence of PNG frames to an AVI file.