/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package abstrata;

/**
 *
 * @author smani
 */
public abstract class Animal {

    private String nome;
    private String especie;
    private int idade;
    
    public Animal() {
    }
    
    public Animal(String nome,String especie,int idade) {
        this.nome = nome;
        this.idade = idade;
        this.especie = especie;
    }
    
    public void Som() {
        System.out.println("fuu");
    }
}
