public class season {
    public static void main(String[] args) {
        System.out.println(getSeason(1));
    }

    public static String getSeason(int month) {
        switch (month) {
            case 1: case 2: case 12: return "冬季";
            case 3: case 4: case 5: return "春季";
            case 6: case 7: case 8: return "夏季";
            case 9: case 10: case 11: return "秋季";
            default: return "无效的月份";
        }
    }
}