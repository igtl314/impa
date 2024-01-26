import java.util.HashMap;
import java.util.Scanner;

public class p315 {
    public void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            doFunc(scanner);
        }
    }


    public void doFunc(Scanner scanner){
        int n;
        try{
            String userInput = scanner.nextLine();
            /*Number of places*/
            n = Integer.parseInt(userInput);
        } catch (NumberFormatException e) {
            throw new RuntimeException(e);
        }
        if (n == 0){
            System.exit(0);
        }
        HashMap<Integer,Integer> map = new HashMap<>();
        for (int i=1; i<=n; i++ ){

        }
    }
}
