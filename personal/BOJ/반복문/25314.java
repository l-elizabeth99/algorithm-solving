// 코딩은 체육과목 입니다
// bronze 5

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine());

    for (int i = 0; i < N/4; i++) {
      System.out.print("long ");
    }
    System.out.println("int");
  }
}
