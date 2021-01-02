
import java.io.*;
import java.sql.*;

class jeo1_sqlite {
    public static void main (String [] args) throws SQLException {
        Connection conn = DriverManager.getConnection("jdbc:sqlite:jeo.db");
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery("select * from users"); 
        //rs.first(); // rs is TYPE_FORWARD_ONLY

        while(rs.next()) {
            System.out.print("name: " + rs.getString("name") + ", ");
            System.out.print("id: " + rs.getString("uuid") + ", ");
            System.out.println();
        }; 

        return;
    }
}

