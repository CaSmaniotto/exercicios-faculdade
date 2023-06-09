package classeGenerica;


public class Generica<tipo> {
    
    private tipo valor;
    
    public void add(tipo valor) {
        this.valor = valor;
    };
    
    public tipo get() {
        return this.valor;
    };
    
};
