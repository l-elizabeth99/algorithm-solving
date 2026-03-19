// 고양이
// bronze 5

import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        bw.write("\\    /\\");
        bw.newLine();
        
        bw.write(" )  ( ')");
        bw.newLine();
        
        bw.write("(  /  )");
        bw.newLine();
        
        bw.write(" \\(__)|");

        bw.flush();
        bw.close();
    }
}
