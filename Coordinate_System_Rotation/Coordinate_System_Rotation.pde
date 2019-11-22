color fill1 = color(225, 225, 225);
color fill2 = color(255, 225, 225);
int h = 400;
int w = 400;
int xo = w/2;
int yo = h/2;
int x[] = {1,0,-1,0};
int y[] = {0,1,0,-1};
int r = 150;

void settings() {
  size(w, h);
}

void setup() {
  background(200);
  drawBg();
}

void draw() {
  
}

void drawBg() {
  noStroke();
  fill(fill1);
  drawCircles(0);
  fill(fill2);
  drawCircles(PI/4);
}

void drawCircles(float rot) {
  for(int i=0; i<4; i++) {
    float xrot = x[i]*r*cos(rot)+y[i]*r*sin(rot);
    float yrot = -x[i]*r*sin(rot)+y[i]*r*cos(rot);
    float circlex = w/2+xrot;
    float circley = h/2+yrot;
    ellipse(circlex,circley,30,30);
  }
}
