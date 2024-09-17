import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class MyWorld here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class MyWorld extends World
{
    private double percentage;
    private boolean juegoEmpezado = false;
    private String texto;
    private String textoFinal;
    
    private Contador score;
    private Contador clicks;
    private Contador misses;
    private AccuracyDisplay accuracy;    
    private CountdownTimer timer;

    
    public MyWorld() {
        super(800, 600, 1);
        score = new Contador("Score: ");
        clicks = new Contador("    ");
        misses = new Contador("Misses: ");
        timer = new CountdownTimer(30);
        
        setPaintOrder(Target.class, Miss.class);
    }
    
    public void inicializarTargets() {
        for (int i = 0; i < 4; i++) {
            Target target = new Target();
            addObject(target, target.getRandomNumber(150, 650), target.getRandomNumber(150, 450));           
        }
    }

    public void act() {
        if (!juegoEmpezado) {
            Greenfoot.playSound("Music.mp3");
            
            inicializarTargets();
            juegoEmpezado = true;
            
            addObject(misses,175,50);
            addObject(clicks, 1000,1000); // Ubicacion lejana
            addObject(score,75,50);
            addObject(timer, 650, 50);
            
        }
        
        if (Greenfoot.mouseClicked(null)) {
            MouseInfo mouse = Greenfoot.getMouseInfo();
            if (mouse != null) {
                int mouseX = mouse.getX();
                int mouseY = mouse.getY();

                if (getObjectsAt(mouseX, mouseY, Target.class).isEmpty()) {
                    Miss miss = new Miss();
                    addObject(miss, mouseX, mouseY);
                    }
                }
            }
        
        if (Greenfoot.mouseClicked(this)) {
            clicks.add(1);
            increaseMisses();
        }
        
        
        if (timer.getTimeLeft() == 0) {
            showPercentage();
            Greenfoot.stop(); 
        }
    }

    public void increaseScore() {
        score.add(1);
    }
    
    public void increaseClicks() {
        clicks.add(1);
    }
    
        public void increaseMisses() {
        misses.add(1);
        Greenfoot.playSound("sonidoMiss.mp3");
    }
    
    public int getMisses(){
        return misses.getValue();
    }
    
    public int getScore() {
        return score.getValue();
    }

    public int getClicks() {
        return clicks.getValue();
    }
    
    private void showPercentage() {
        removeObject(clicks);
        removeObject(timer);
        removeObject(misses);
        removeObjects(getObjects(Target.class));
        
        accuracy = new AccuracyDisplay();
        Greenfoot.playSound("sonidoFinal.mp3");
        score.setLocation(400,250);
        addObject(accuracy, 400, 300);
        }
    }
