from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time

# Window dimensions
width, height = 800, 600

# Rainbow state
current_band = 0

# Rainbow colors (VIBGYOR - from inner to outer)
rainbow_colors = [
    (0.56, 0.0, 1.0),   # Violet
    (0.29, 0.0, 0.51),  # Indigo
    (0.0, 0.0, 1.0),    # Blue
    (0.0, 1.0, 0.0),    # Green
    (1.0, 1.0, 0.0),    # Yellow
    (1.0, 0.5, 0.0),    # Orange
    (1.0, 0.0, 0.0),    # Red
]

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)

def draw_arc(center_x, center_y, inner_radius, thickness, start_angle, end_angle, color):
    glColor3f(*color)
    glBegin(GL_TRIANGLE_STRIP)
    for angle in range(start_angle, end_angle + 1):
        rad = math.radians(angle)
        x_outer = center_x + (inner_radius + thickness) * math.cos(rad)
        y_outer = center_y + (inner_radius + thickness) * math.sin(rad)
        x_inner = center_x + inner_radius * math.cos(rad)
        y_inner = center_y + inner_radius * math.sin(rad)
        glVertex2f(x_outer, y_outer)
        glVertex2f(x_inner, y_inner)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    center_x = width // 2
    center_y = 100
    inner_radius = 100
    arc_thickness = 20
    start_angle = 0
    end_angle = 180

    for i in range(current_band):
        draw_arc(center_x, center_y, inner_radius + i * arc_thickness, arc_thickness, start_angle, end_angle, rainbow_colors[i])

    glFlush()

def update(value):
    global current_band
    if current_band < len(rainbow_colors):
        current_band += 1
        glutPostRedisplay()
        glutTimerFunc(600, update, 0)  # Delay between each band (ms)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Animated Rainbow Formation")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(600, update, 0)  # Start animation
    glutMainLoop()

if __name__ == "__main__":
    main()






