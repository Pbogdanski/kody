function setup() {
  createCanvas(10000,10000);
}

// function draw() {
//
//   strokeWeight(4);
//   stroke("#2A31FF");
//   fill(255, 0, 0);
//   ellipse(500, 150, 80, 80);
//
//   strokeWeight(15);
//   stroke("#FF40CF");
//   fill(0, 150, 0);
//   ellipse(100, 100, 200, 80);
//
//   strokeWeight(8);
//   stroke("#FFED3D");
//   fill(0, 0, 300);
//   rect(300, 200, 55, 55);

  noFill();
  noStroke();
  if (mouseIsPressed) {
    if(mouseButton === LEFT)
      r = random(255);
      g = random(255);
      b = random(255);
      strokeWeight(10);
      fill(r, g, b);
      stroke(r, g, b);
  }
  if <mouseButton === CENTER) {
    strokeWeight(20);
    fill(255, 255, 255);
    stroke(255, 255, 255);
    rect(mouseX-10, mouseY-10, 20, 20);

  } else {
    noFill();
    noStroke();
    }
    point(mouseX, mouseY);
  }
