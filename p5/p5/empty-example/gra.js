  function setup() {
  createCanvas(10000,10000);
      
}

  function mouseClicked() {
    if (mouseButton === LEFT) {
        rect(mouseX-10, mouseY-10, 20, 20);
      }else{
      eclipse(mouseX-10, mouseY-10, 20, 30);
      }

  }
