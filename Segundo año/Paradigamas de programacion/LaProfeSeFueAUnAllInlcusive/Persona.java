public class Persona
{
    private String nombre;
    private String apellido;
    private String email;
    private int numeroDeTelefono;

    public Persona()
    {

    }

    public void setEmail(String email){
        this.email = email;
    }
    
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    
    public void setApellido(String apellido){
        this.apellido = apellido;
    }
    
    public void setNumeroDeTelefono(int numeroDeTelefono ){
        this.numeroDeTelefono = numeroDeTelefono;
    }
    
    public String getEmail(){
        return email;
    }
    
    public String getNombre(){
        return nombre;
    }
    
    public String getApellido(){
        return apellido;
    }
    
    public int getsetNumeroDeTelefono(){
        return numeroDeTelefono;
    }
}
