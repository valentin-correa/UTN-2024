import greenfoot.*;

public class Target extends Actor
{
    private int targetsHitted = 0;
    private CountdownTimer timer;  
    private long moveTime = 2; // Tiempo de inicio de los targets
    
    public Target(){
        timer = new CountdownTimer(moveTime);
    }
    
    public void act()
    {
            if (Greenfoot.mouseClicked(this)) {
            Greenfoot.playSound("sonidoHit.mp3");
            setLocation(getRandomNumber(150,650), getRandomNumber(150,450));
            MyWorld world = (MyWorld) getWorld();
            world.increaseScore();
            world.increaseClicks();
            timer.setStartTime();
        }
        else if(timer.getTimeLeft() == 0){
            setLocation(getRandomNumber(150,650), getRandomNumber(150,450));
            timer.setStartTime();
        }
    }
    
    public int getRandomNumber(int start,int end)
{
       int normal = Greenfoot.getRandomNumber(end-start+1);
       return normal+start;
}
    
}
