package org.example;

import org.example.Modelos.Articulo;
import org.example.Modelos.DetallePedido;
import org.example.Modelos.Pedido;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Articulo> articulosDisponibles = new ArrayList<>();
        ArrayList<DetallePedido> detallesPedido = new ArrayList<>();
        Pedido pedido = new Pedido();

        // Agregar algunos artículos por defecto
        articulosDisponibles.add(new Articulo("Fideo", 100));
        articulosDisponibles.add(new Articulo("Arroz", 200));

        boolean x = true;

        while (x) {
            System.out.println("\nMenú:");
            System.out.println("0 - Salir");
            System.out.println("1 - Agregar artículo al pedido");
            System.out.println("2 - Registrar pedido y calcular total");

            System.out.print("Selecciona una opción: ");
            int opcion = scanner.nextInt();

            switch (opcion) {
                case 0:
                    x = false;
                    System.out.println("Ha salido del sistema");
                    break;
                case 1:
                    System.out.println("Artículos disponibles:");
                    for (int i = 0; i < articulosDisponibles.size(); i++) {
                        System.out.println(i + " - " + articulosDisponibles.get(i).getNombre() + " - Precio: " + articulosDisponibles.get(i).getPrecio());
                    }
                    System.out.print("Selecciona el artículo por su número: ");
                    int posicionArticulo = scanner.nextInt();

                    if (posicionArticulo >= 0 && posicionArticulo < articulosDisponibles.size()) {
                        Articulo articuloSeleccionado = articulosDisponibles.get(posicionArticulo);
                        System.out.print("Ingresa la cantidad para el artículo " + articuloSeleccionado.getNombre() + ": ");
                        int cantidad = scanner.nextInt();

                        DetallePedido detalle = new DetallePedido(cantidad, articuloSeleccionado);
                        detallesPedido.add(detalle);
                        pedido.agregarDetalle(detalle);
                        System.out.println("Artículo agregado al pedido");
                    } else {
                        System.out.println("Selección de artículo no válida");
                    }
                    break;
                case 2:
                    if (detallesPedido.isEmpty()) {
                        System.out.println("No hay artículos en el pedido");
                    } else {
                        double totalVenta = pedido.calcularTotal();
                        System.out.println("El Total de la venta es: " + totalVenta);
                    }
                    break;
                default:
                    System.out.println("Opción no válida");
                    break;
            }
        }
        scanner.close();
    }
}
