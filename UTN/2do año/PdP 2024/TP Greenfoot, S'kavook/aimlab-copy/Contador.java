import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class contador here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Contador extends Actor
{
    private int value = 0;
    private int target = 0;
    private String text;
    private int stringLength;
    
    public Contador(){
        this("");
    }
    
    public Contador(String texto){
        text = texto;
        stringLength = (text.length() +2) * 16;
        
        setImage(new GreenfootImage(stringLength,12));
        GreenfootImage image = getImage();
        Font font = image.getFont();
        image.setFont(font.deriveFont(12.0F));
        image.setColor(Color.BLACK);
        
        updateImage();
     }
     
    /**
     * Act - do whatever the contador wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act()
    {
        if(value < target) {
            value++;
            updateImage();
        }else if(value > target) {
            value--;
            updateImage();
        }// Add your action code here.
    }
    
    public void add(int score){
        target += score;
    }
    
    public void subtract(int score){
        target -= score;
    }
    
    public int getValue(){
        return value;
    }
    
    public void setValue(int newValue){
        value = newValue;
    }
    
    private void updateImage(){
        GreenfootImage image = new GreenfootImage(text + value, 24, Color.BLACK, new Color(0,0,0,0));
        setImage(image);
    }
}
