import greenfoot.*;

public class CountdownTimer extends Actor {
    private long startTime;
    private final long countdownTime; // Tiempo inicial

    public CountdownTimer(long time) {
        countdownTime = time;
        startTime = System.currentTimeMillis();  // Tiempo inicio
        updateImage(countdownTime);  // Inicializa el temporizador
    }

    public void act() {
        // Calcula el tiempo transcurrido desde el inicio
        long elapsedTime = (System.currentTimeMillis() - startTime) / 1000; // Tiempo transcurrido en segundos
        long timeLeft = countdownTime - elapsedTime; // Calcula el tiempo restante

        if (timeLeft <= 0) {
            timeLeft = 0;
        }
        
        updateImage(timeLeft);
    }

    private void updateImage(long timeLeft) { // Muestra el temporizador
        GreenfootImage image = new GreenfootImage("Time Left: " + timeLeft + " seconds", 24, Color.BLACK, new Color(0, 0, 0, 0));
        setImage(image);
    }

    public void setStartTime(){
        this.startTime = System.currentTimeMillis();
        updateImage(countdownTime);
    }
    
    public long getTimeLeft() {
        long elapsedTime = (System.currentTimeMillis() - startTime) / 1000; // Tiempo transcurrido en segundos
        long timeLeft = countdownTime - elapsedTime; // Calcula el tiempo restante
        return Math.max(timeLeft, 0); // Devuelve el tiempo restante en segundos
    }
}
