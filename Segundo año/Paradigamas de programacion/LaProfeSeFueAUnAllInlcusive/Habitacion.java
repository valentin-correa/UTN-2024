public class Habitacion
{
    private int nroHabitacion;
    private TipoHabitacion tipo;
    private Acceso ingreso;
    
    private String clave;
    public Habitacion()
    {
        clave = ingreso.getCodigoDeAcceso();
    }

    public boolean verificarClaveDeAcceso(String clave)
    {
        if (clave == this.clave) {
            return true;
            registrarAcceso();
        }
        else {
            return false;
        }
    }
    
    private void registrarAcceso() {
        
    }
    
}
