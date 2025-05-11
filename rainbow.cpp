#include <GL/glut.h>
#include <math.h>

void init(void) {
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(0.0, 400.0, 0.0, 400.0);
}

void drawRainbow(void) {
    glClear(GL_COLOR_BUFFER_BIT);

    float radius = 150.0;
    float centerX = 200.0;
    float centerY = 100.0;
    int segments = 100;

    float colors[7][3] = {
        {1.0, 0.0, 0.0},
        {1.0, 0.5, 0.0},
        {1.0, 1.0, 0.0},
        {0.0, 1.0, 0.0},
        {0.0, 0.0, 1.0},
        {0.3, 0.0, 0.5},
        {0.5, 0.0, 1.0}
    };

    for (int color = 0; color < 7; color++) {
        glColor3fv(colors[color]);
        glLineWidth(10.0);

        glBegin(GL_LINE_STRIP);
        for (int i = 0; i <= segments / 2; i++) {
            float angle = (float)i / (float)segments * 3.14159;
            float x = centerX + radius * cos(angle);
            float y = centerY + radius * sin(angle);
            glVertex2f(x, y);
        }
        glEnd();

        radius -= 15.0;
    }

    glFlush();
}

void display(void) {
    drawRainbow();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(400, 400);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Rainbow using OpenGL");

    init();
    glutDisplayFunc(display);
    glutMainLoop();

    return 0;
}








// background colors:
//when all are 0.0-black
//when {0.0,1.0,0.0,0.0}-green
//when{ 1.0,0.0,0.0,0.0 }-red
//when {0.0,0.0,1.0,0.0}-blue
//when {0.0,0.0,1.0,1.0}-black
//when {1.0,1.0,1.0,1.0}-white

