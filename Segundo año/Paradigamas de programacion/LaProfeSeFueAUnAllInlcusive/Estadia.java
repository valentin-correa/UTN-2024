public class Estadia
{
    private int nroEstadia;
    private int fechaIngreso;
    private int fechaEgresoPrevista;
    private Habitacion habitacion;
    private int codigoAccesoHuesped;
    private int fechaDeEgresoReal;
    private double precioPorNocheHistorico;
    private int diasEstadia;
   
    public Estadia()
    {
        
    }

    public Habitacion conocerHabitacion() {
        return habitacion;//Supongo que los datos que sean nesesarios de la clase habitacion
    }
    
    public int calcularDiasDeEstadia() {
        return diasEstadia = fechaEgresoPrevista - fechaIngreso;
    }
    
    public void registrarEgreso() {
        
    }
    
    public void calcularImporteTotal() {
        
    }
    
    public int getNroEstadia() {
        return nroEstadia;
    }

    public void setNroEstadia(int nroEstadia) {
        this.nroEstadia = nroEstadia;
    }

    public int getFechaIngreso() {
        return fechaIngreso;
    }

    public void setFechaIngreso(int fechaIngreso) {
        this.fechaIngreso = fechaIngreso;
    }

    public int getFechaEgresoPrevista() {
        return fechaEgresoPrevista;
    }

    public void setFechaEgresoPrevista(int fechaEgresoPrevista) {
        this.fechaEgresoPrevista = fechaEgresoPrevista;
    }

    public Habitacion getHabitacion() {
        return habitacion;
    }

    public void setHabitacion(Habitacion habitacion) {
        this.habitacion = habitacion;
    }

    public int getCodigoAccesoHuesped() {
        return codigoAccesoHuesped;
    }

    public void setCodigoAccesoHuesped(int codigoAccesoHuesped) {
        this.codigoAccesoHuesped = codigoAccesoHuesped;
    }

    public int getFechaDeEgresoReal() {
        return fechaDeEgresoReal;
    }

    public void setFechaDeEgresoReal(int fechaDeEgresoReal) {
        this.fechaDeEgresoReal = fechaDeEgresoReal;
    }

    public double getPrecioPorNocheHistorico() {
        return precioPorNocheHistorico;
    }

    public void setPrecioPorNocheHistorico(double precioPorNocheHistorico) {
        this.precioPorNocheHistorico = precioPorNocheHistorico;
    }
}
