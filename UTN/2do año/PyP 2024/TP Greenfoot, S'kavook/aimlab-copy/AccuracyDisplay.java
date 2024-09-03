import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class AccuracyDisplay extends Actor {
    private int percentage;
    private int clicks;
    private int score;
    
    public AccuracyDisplay(){
        
    }
    
    public void addedToWorld(World world) {
        MyWorld mundo = (MyWorld) world;
        
        score = mundo.getScore();
        clicks = mundo.getClicks();
        
        if (clicks > 0) {
            percentage = score * 100 / clicks;
        } else {
            percentage = 0;
        }

        updateImage();
    }

    private void updateImage() {
        setImage(new GreenfootImage("Accuracy: " + percentage + "%", 24, Color.BLACK, new Color(0, 0, 0, 0)));
    }
}