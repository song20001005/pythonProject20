# pythonProject20
yuan02
这是猿人学的第二题，通过网页抓包可以看到网页请求了两次，第一次得到的是一段混淆过后加密代码，通过事件监听断点script在第一次请求时使用以下hook代码 。找到生成cookie的关键代码，手动解混淆后，通过报错信息慢慢补函数(这里有个防止格式化，以及修改了内部函数功能的反调)

Object.defineProperty(document, 'cookie', {
  set: function(val) {
      console.log('cookie的值:', val);
      debugger
      return val;
    }
  }
) 

