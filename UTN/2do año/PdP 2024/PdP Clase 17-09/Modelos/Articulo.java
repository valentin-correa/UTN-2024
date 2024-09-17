package org.example.Modelos;

public class Articulo {
    private String nombre;
    private double precioUnitario;

    public Articulo() {
    }

    public Articulo(String nombre, double precioUnitario) {
        this.nombre = nombre;
        this.precioUnitario = precioUnitario;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getPrecioUnitario() {
        return precioUnitario;
    }

    public void setPrecioUnitario(double precioUnitario) {
        this.precioUnitario = precioUnitario;
    }

    public String toString(){
        return "Nombre: "+this.nombre
                +"\n$"+this.precioUnitario;
    }

    public double getPrecio(){
        return precioUnitario;
    }
}
