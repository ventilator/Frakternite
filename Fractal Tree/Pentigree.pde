/** 
 * Pentigree L-System 
 * by Geraldine Sarmiento. 
 * 
 * This code was based on Patrick Dwyer's L-System class. 
 */
 

PentigreeLSystem ps;

void setup() {
  
  size(800, 800);
  background(0);
  ps = new PentigreeLSystem(90);
  PentigreeLSystem ps2 = new PentigreeLSystem(-90);
  ps.simulate(4);
  ps2.simulate(4);
  pushMatrix();
  ps.render();
  popMatrix();
  ps2.render();
  save("CON");
  
  
  
  
}

void draw() {
  
}
