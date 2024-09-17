package org.example.Modelos;

import java.util.ArrayList;

public class Pedido {
    private ArrayList<DetallePedido> detalles = new ArrayList<>();

    public ArrayList<DetallePedido> getDetalles() {
        return detalles;
    }

    public void setDetalles(ArrayList<DetallePedido> detalles) {
        this.detalles = detalles;
    }

    public void agregarDetalle(DetallePedido detalle){
        this.detalles.add(detalle);
    }

    public double calcularTotal(){
        double acumulador=0;
        for (DetallePedido d : detalles){
            acumulador += d.calcularSubTotal();
        }
        return acumulador;
    }

}
