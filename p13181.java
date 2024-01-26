import java.io.*;
import java.util.*;


public class p13181 {

    public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        while (true){
            try {
                String line = reader.readLine();
                if (line == null || line.isEmpty()) {
                    break;
                }
                solve(line);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }


    private static void solve(String line) {
        int temp = 0;
        int furthest = 0;
        boolean firstbed = false;

        for (int i = 0; i < line.length(); i++) {
           if (line.charAt(i) == 'X'){
            if (!firstbed){
                if (temp > furthest){
                    furthest = temp-1;
                }
                firstbed = true;
            }
            else if (firstbed){
                if (temp%2 == 0){
                    temp--;
                }
                if (temp > furthest){
                    furthest = (int)Math.floor(temp/2);
                }
            }
            temp = 0;
            }
            else if (line.charAt(i) == '.'){
                temp++;
            }
        }
        System.out.println(furthest);
    }
    
}
