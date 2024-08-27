import java.util.Date;

public class Acceso{
    private Date fecha;
    private String codigoDeAcceso;
    
    public Acceso(){
    
    }
    
    public void setCodigoDeAcceso(String codigo) {
        codigoDeAcceso = codigo;
    }
    
    public String getCodigoDeAcceso() {
        return codigoDeAcceso;
    }
}