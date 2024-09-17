package org.example.Modelos;

public class DetallePedido {
    private int cantidad;
    private Articulo articulo;

    public DetallePedido() {
    }

    public DetallePedido(int cantidad, Articulo articulo) {
        this.cantidad = cantidad;
        this.articulo = articulo;
    }

    public int getCantidad() {
        return cantidad;
    }

    public void setCantidad(int cantidad) {
        this.cantidad = cantidad;
    }

    public Articulo getArticulo() {
        return articulo;
    }

    public void setArticulo(Articulo articulo) {
        this.articulo = articulo;
    }

    public String toString() {
        return "DetallePedido{" +
                "cantidad=" + cantidad +
                ", articulo=" + articulo +
                '}';
    }

    public double calcularSubTotal(){
        return this.articulo.getPrecioUnitario()*this.cantidad;
    }
}
