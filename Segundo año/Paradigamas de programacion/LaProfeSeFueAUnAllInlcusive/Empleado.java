public class Empleado extends Persona{
    private int idEmpleado; // Como es en este caso
    private Rol rol; // y en este
    private String codigoAccesoEmpleado;
    
    public Empleado(){
        
    }
    
    public Empleado(Rol rol, int idEmpleado){
        this.rol = rol;
        
    }
    
    public void setCodigoAccesoEmpleado(String codigoAccesoEmpleado){
        this.codigoAccesoEmpleado = codigoAccesoEmpleado;
    }
    
    public String getCodigoAccesoEmpleado(){
        return codigoAccesoEmpleado;
    }
}