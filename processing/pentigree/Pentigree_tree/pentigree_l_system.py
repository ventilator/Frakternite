from l_system import LSystem


class PentigreeLSystem(LSystem):
           
    def __init__(self):
        self.steps = 0      
        self.somestep = 0.1
        self.xoff = 0.01
        self.axiom = "F"
        self.rule = "F[-F][+F]"
        self.startLength = 60.0
        self.theta = radians(35)
        self.reset()

    def useRule(self, r_):
        self.rule = r_

    def useAxiom(self, a_):
        self.axiom = a_

    def useLength(self, l_):
        self.startLength = l_

    def useTheta(self, t_):
        self.theta = radians(t_)

    def reset(self):
        self.production = self.axiom
        self.drawLength = self.startLength
        self.generations = 0

    def getAge(self):
        return self.generations

    def render(self):                
        translate(width / 4, height / 2)
        self.steps += 3
        if self.steps > len(self.production):
            self.steps = len(self.production)

        recursion_level = 1
        for i in range(self.steps):
            step = self.production[i]            
            hue_ = recursion_level*30 # color to cycle through, for each push 
            if step == 'F':
                noFill()
                stroke(hue_,255,255)
                line(0, 0, 0, -self.drawLength)
                translate(0, -self.drawLength)
            elif step == '+':
                rotate(self.theta)
            elif step == '-':
                rotate(-self.theta)
            elif step == '[':
                pushMatrix()
                recursion_level += 1
            elif step == ']':
                popMatrix()
                recursion_level -= 1
