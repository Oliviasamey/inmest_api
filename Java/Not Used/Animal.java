public class Animal {
    String name = "anime";
    String owner = "Tom";

    void displayAnimalName(){
        System.out.println("Name of animal" + name);
    }

    void displayOwnerName(){
        System.out.println("Name of Owner" + owner);
    }
    
    /**
     * get the name of the animal
     * @return String, the name of the animal
     */
    String getAnimalName() {
        return name;
    }
}
