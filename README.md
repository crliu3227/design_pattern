# design_pattern

使用python学习设计模式

=========================================================

## Singleton.py:单例模式

单例模式是所有设计模式中比较简单的一类，其定义如下：Ensure a class has only one instance, and provide a global point of access to it.（保证某一个类只有一个实例，而且在全局只有一个访问点）

单例模式的优点：

1. 由于单例模式要求在全局内只有一个实例，因而可以节省比较多的内存空间；
2. 全局只有一个接入点，可以更好地进行数据同步控制，避免多重占用；
3. 单例可长驻内存，减少系统开销。

单例模式的缺点：

1. 单例模式的扩展是比较困难的；
2. 赋于了单例以太多的职责，某种程度上违反单一职责原则（六大原则后面会讲到）；
3. 单例模式是并发协作软件模块中需要最先完成的，因而其不利于测试；
4. 单例模式在某种情况下会导致“资源瓶颈”。

单例模式的应用举例：

1. 生成全局惟一的序列号；
2. 访问全局复用的惟一资源，如磁盘、总线等；
3. 单个对象占用的资源过多，如数据库等；
4. 系统全局统一管理，如Windows下的Task Manager；
5. 网站计数器。

## factory.py: 工厂模式

工厂模式的定义如下：定义一个用于创建对象的接口，让子类决定实例化哪个类。工厂方法使一个类的实例化延迟到其子类。

工厂模式的优点：

1. 一个调用者想创建一个对象，只要知道其名称就可以了；
2. 扩展性高，如果想增加一个产品，只要扩展一个工厂类就可以;
3. 屏蔽产品的具体实现，调用者只关心产品的接口。

工厂模式的缺点：

1. 每次增加一个产品时，都需要增加一个具体类和对象实现工厂，使得系统中类的个数成倍增加，在一定程度上增加了系统的复杂度，同时也增加了系统具体类的依赖。

工厂模式应用举例：

1. 设计一个连接服务器的框架，需要三个协议，"POP3"、"IMAP"、"HTTP"，可以把这三个作为产品类，共同实现一个接口。

## builer.py: 建造者模式

建造者模式的定义如下：将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。

建造者模式的优点：

1. 封装性好，用户可以不知道对象的内部构造和细节，就可以直接建造对象；
2. 系统扩展容易；
3. 建造者模式易于使用，非常灵活。在构造性的场景中很容易实现“流水线”；
4. 便于控制细节。

建造者模式的缺点：

1. “加工工艺”对用户不透明。（封装的两面性）

建造者模式应用举例：

1. 去肯德基，汉堡、可乐、薯条、炸鸡翅等是不变的，而其组合是经常变化的，生成出所谓的"套餐"。

## prototype.py: 原型模式

原型模式定义如下：用原型实例指定创建对象的种类，并且通过复制这些原型创建新的对象。
需要注意一点的是，进行clone操作后，新对象的构造函数没有被二次执行，新对象的内容是从内存里直接拷贝的。

原型模式的优点：

1. 性能极佳，直接拷贝比在内存里直接新建实例节省不少的资源；
2. 简化对象创建，同时避免了构造函数的约束，不受构造函数的限制直接复制对象，是优点，也有隐患，这一点还是需要多留意一些。

原型模式的缺点：

1. 深拷贝和浅拷贝的使用需要事先考虑周到；
2. 某些编程语言中，拷贝会影响到静态变量和静态函数的使用。

原型模式应用举例：

1. 对象在修改过后，需要复制多份的场景。如一些涉及到复制、粘贴的场景。

## proxy.py: 代理模式

代理模式定义如下：为某对象提供一个代理，以控制对此对象的访问和控制。代理模式在使用过程中，应尽量对抽象主题类进行代理，而尽量不要对加过修饰和方法的子类代理。

代理模式的优点：

1. 职责清晰：非常符合单一职责原则，主题对象实现真实业务逻辑，而非本职责的事务，交由代理完成；
2. 扩展性强：面对主题对象可能会有的改变，代理模式在不改变对外接口的情况下，可以实现最大程度的扩展；
3. 保证主题对象的处理逻辑：代理可以通过检查参数的方式，保证主题对象的处理逻辑输入在理想范围内。

代理模式的缺点：

1. 可能会降低整体业务的处理效率和速度。

代理模式应用举例：

1. 针对某特定对象进行功能和增强性扩展。如IP防火墙、远程访问代理等技术的应用；
2. 对主题对象进行保护。如大流量代理，安全代理等；

## wrapper.py: 装饰器模式

装饰器模式定义如下：动态地给一个对象添加一些额外的职责。在增加功能方面，装饰器模式比生成子类更为灵活。

装饰器模式的优点：

1. 装饰器模式是继承方式的一个替代方案，可以轻量级的扩展被装饰对象的功能；
2. Python的装饰器模式是实现AOP的一种方式，便于相同操作位于不同调用位置的统一管理。

装饰器模式的缺点：

1. 多层装饰器的调试和维护有比较大的困难。

装饰器模式应用举例：

1. 需要扩展、增强或者减弱一个类的功能。

## adapter.py: 适配器模式

适配器模式定义如下：将一个类的接口变换成客户端期待的另一种接口，从而使原本因接口不匹配而无法在一起工作的两个类能够在一起工作。
适配器模式和装饰模式有一定的相似性，都起包装的作用，但二者本质上又是不同的，装饰模式的结果，是给一个对象增加了一些额外的职责，而适配器模式，则是将另一个对象进行了“伪装”。

适配器模式的优点：

1. 适配器模式可以让两个接口不同，甚至关系不大的两个类一起运行；
2. 提高了类的复用度，经过“伪装”的类，可以充当新的角色；
3. 适配器可以灵活“拆卸”。

适配器模式的缺点：

1. 适配器模式与原配接口相比，毕竟增加了一层调用关系，所以，在设计系统时，不要使用适配器模式。

适配器应用举例：

1. 不修改现有接口，同时也要使该接口适用或兼容新场景业务中，适合使用适配器模式。
例如，在一个嵌入式系统中，原本要将数据从Flash读入，现在需要将数据从磁盘读入，
这种情况可以使用适配器模式，将从磁盘读入数据的接口进行“伪装”，以从Flash中读数据的接口形式，从磁盘读入数据。

## facade.py: 门面模式

门面模式也叫外观模式，定义如下：要求一个子系统的外部与其内部的通信必须通过一个统一的对象进行。
门面模式提供一个高层次的接口，使得子系统更易于使用。门面模式注重“统一的对象”，也就是提供一个访问子系统的接口。

门面模式的优点：

1. 减少了系统之间的相互依赖，提高了系统的灵活；
2. 提高了整体系统的安全性：封装起的系统对外的接口才可以用，隐藏了很多内部接口细节，若方法不允许使用，则在门面中可以进行灵活控制。

门面模式的缺点：

1. 门面模式的缺点在于，不符合开闭原则，一旦系统成形后需要修改，几乎只能重写门面代码，这比继承或者覆写等方式，或者其它一些符合开闭原则的模式风险都会大一些。

门面模式应用举例：

1. 为一个复杂的子系统提供一个外界访问的接口。这类例子是生活还是蛮常见的，例如电视遥控器的抽象模型，电信运营商的用户交互设备等；

## composite.py: 组合模式

组合模式也叫作部分-整体模式，其定义如下：将对象组合成树形结构以表示“部分”和“整体”的层次结构，使得用户对单个对象和组合对象的使用具有一致性。

组合模式的优点：

1. 节点增加和减少是非常自由和方便的，这也是树形结构的一大特点；
2. 所有节点，不管是分支节点还是叶子结点，不管是调用一个结点，还是调用一个结点群，都是非常方便的。

组合模式的缺点：

1. 由于叶子结点和分支结点直接使用了实现类，而不方便使用抽象类，这大大限制了接口的影响范围；若结点接口发生变更，对系统造成的风险会比较大。

组合模式应用举例：

1. 维护部分与整体的逻辑关系，或者动态调用整体或部分的功能接口，可以考虑使用组合模式。例如，非常多的操作系统（如Linux）都把文件系统设计成树形结构。

## flyweight.py: 享元模式

享元模式定义如下：使用共享对象支持大量细粒度对象。大量细粒度的对象的支持共享，可能会涉及这些对象的两类信息：内部状态信息和外部状态信息。内部状态信息就是可共享出来的信息，它们存储在享元对象内部，不会随着特定环境的改变而改变；外部状态信息就不可共享的信息了。享元模式中只包含内部状态信息，而不应该包含外部状态信息。

享元模式的优点：

1. 减少重复对象，大大节约了系统资源。

享元模式的缺点：

1. 享元模式虽然节约了系统资源，但同时也提高了系统的复杂性，尤其当遇到外部状态和内部状态混在一起时，需要先将其进行分离，才可以使用享元模式。否则，会引起逻辑混乱或业务风险；
2. 享元模式中需要额外注意线程安全问题。

享元模式应用举例：

1. 需要缓冲池的场景中，可以使用享元模式。如进程池，线程池等技术，就可以使用享元模式

## bridge.py: 桥接模式

桥接模式，定义如下：将抽象与实现解耦（注意此处的抽象和实现，并非抽象类和实现类的那种关系，而是一种角色的关系，这里需要好好区分一下），可以使其独立变化。抽象化角色和实现化角色是解耦的，这也就意味着，所谓的桥，就是抽象化角色的抽象类和实现化角色的抽象类之间的引用关系。

桥接模式的优点：

1. 抽象角色与实现角色相分离，二者可以独立设计，不受约束；
2. 扩展性强：抽象角色和实现角色可以非常灵活地扩展。

桥接模式的缺点：

1. 增加对系统理解的难度。

桥接模式的应用举例：

1. 不适用继承或者原继承关系中抽象类可能频繁变动的情况，可以将原类进行拆分，拆成实现化角色和抽象化角色。
2. 重用性比较大的场景。比如开关控制逻辑的程序，开关就是抽象化角色，开关的形式有很多种，操作的实现化角色也有很多种，采用桥梁模式，（如当前例子）开关即可进行复用，整体会将设计的粒度减小。

## strategy.py: 策略模式

策略模式定义如下：定义一组算法，将每个算法都封装起来，并使他们之间可互换。

策略模式的优点：

1. 各个策略可以自由切换：这也是依赖抽象类设计接口的好处之一；
2. 减少代码冗余；
3. 扩展性优秀，移植方便，使用灵活。

策略模式的缺点：

1. 项目比较庞大时，策略可能比较多，不便于维护；
2. 策略的使用方必须知道有哪些策略，才能决定使用哪一个策略，这与迪米特法则是相违背的。

策略模式的应用举例：

1. 算法策略比较经常地需要被替换时，可以使用策略模式。如现在超市前台，会常遇到刷卡、某宝支付、某信支付等方式，就可以参考策略模式。

## chain.py: 责任链模式

责任链模式的定义如下：使多个对象都有机会处理请求，从而避免了请求的发送者和接收者之间的耦合关系。将这些对象连成一条链，并沿着这条链传递该请求，直到有对象处理它为止。

责任链模式的优点：

1. 将请求者与处理者分离，请求者并不知道请求是被哪个处理者所处理，易于扩展。

责任链模式的缺点：

1. 如果责任链比较长，会有比较大的性能问题；
2. 如果责任链比较长，若业务出现问题，比较难定位是哪个处理者的问题。

责任链模式的应用举例：

1. 银行的客户请求处理系统也可以用责任链模式实现（VIP客户和普通用户处理方式当然会有不同）。
2. WSGI框架


