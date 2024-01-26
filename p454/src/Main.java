import java.io.*;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;

public class Main {

    private static String preprocess(String s){
        char [] c = new char[s.length()];
        int cCount = 0;
        for (int i = 0; i<s.length();i++){
            if (s.charAt(i) != ' '){
                c[cCount++] = s.charAt(i);
            }
        }
        Arrays.sort(c,0,cCount);
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<cCount;i++) {
            sb.append(c[i]);
        }
        return  sb.toString();
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       // String filePath = "output.txt";
       //BufferedWriter writer = new BufferedWriter(new FileWriter(filePath));

        int testCaseCount = Integer.parseInt(br.readLine());
        br.readLine();

        for (int testCase = 0; testCase<testCaseCount; testCase++){
            ArrayList<String> sList = new ArrayList<>();
            String s;
            while((s= br.readLine()) != null && !s.equals("")){
                sList.add(s);
            }
            String [] sAr = sList.toArray(new String[sList.size()]);
            Arrays.sort(sAr);
            String [] key = new String[sAr.length];

            for (int i = 0; i< sAr.length; i++){
                key[i]=preprocess(sAr[i]);
            }

            ArrayList<String> toDisplay = new ArrayList<String>();
            for (int i = 0; i< sAr.length;i++ ){
                for (int j = i+1; j<sAr.length; j++){
                    if (key[i].equals(key[j])){
                        StringBuilder sb = new StringBuilder(sAr[i]);
                        sb.append(" = ");
                        sb.append(sAr[j]);
                        toDisplay.add(sb.toString());
                    }
                }
            }
            Collections.sort(toDisplay);
            StringBuilder sb = new StringBuilder();
            Iterator<String> it = toDisplay.iterator();
            if (it.hasNext()) {
                while (it.hasNext()) {
                    sb.append(it.next());
                    if (it.hasNext()) {
                        sb.append("\n");
                    }
                }
                System.out.println(sb.toString());
                //writer.write(sb.toString());
                if((testCase+1)<testCaseCount){
                    System.out.println();

                }


            }

        }
     //   writer.close();
    }
}