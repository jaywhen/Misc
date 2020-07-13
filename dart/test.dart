main() {
  /* 很基础的语法 */
  print('hello');

  String hi = "hi";
  String namee = "when";
  print("$hi $namee"); //连接两个字符串，也可用 '+'

  //Map
  var person = {"name": "mozart", "age": 20};

  var people = new Map();
  people["name"] = "Lister";
  people["age"] = 20;

  print(person);
  print(people);
  print(people["name"]);

  //List
  var tabel = ["itema", "itemb", 12];
  print(tabel);
  tabel.add(13);
  print(tabel);

  var the_table = new List();
  var war = new List<int>();
  war.add(23);
  print(war);

  the_table.add(1);
  the_table.add(2);
  print(the_table);

  //若a为空，则给a赋值为30
  var a;
  a ??= 30;
  print(a);

  var b = 220;
  b ??= 20;
  print(b);
}
