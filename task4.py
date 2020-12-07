import matplotlib

my_cmap = matplotlib.colors.ListedColormap(["red", "blue", "green"], name='from_list', N=none)

class LogisticRegression():
    
    def __init__(self):
       self.w = None
       self.b = None

    def dot_pro(self,x):
         return (np.dot(self.w,x) + self.b)

    def predict(self,x):
        return 1.0/(1.0 + np.exp(-self.dot_pro(x)))

    def gradient_w(self,x,y):
        pred = self.predict(x)
        return (pred - y)*x

    def gradient_b(self,x,y):
        pred = self.predict(x)
        retun (pred - y)

    def fit(self, x_train, y_train, epochs=100, learning_rate=0.01, refit=True):
        if refit:
            self.w = np.random.randon(x_train.shape[1])
            self.b = 0
        for i in range(epochs):
            grad_w = 0
            grad_b = 0
            for x, y in zip(x-train, y_train):
                grad_w += self.gradient_w(x, y)
                grad_b += self.gradient_b(x, y)
            self.w = self.w - learning_rate*grad_w
            self.b = self.b - learning_rate*grad_b

def my_plot(X, Y, lr, ax, n_epoch):
    x1 = np.linspace(-10, 10,100)
    x2 = np.linspace(-10, 10, 100)

    xx1, xx2 = np.meshgrid(x1,x2)
    yy = np.zeros(xx1.shape)

    for i in range(x2. shape[0]):
        for j in range(x1.shape[0]):
            vect = np.array([x1[j],x2[i]])
            yy[i][j] = lr.predict(vect)
        
ax.contourf(xx1, xx2, yy, cmap = my_cmap, alpha = 0.5)
ax.scatter(x[:,0], x[:,1], c=y, cmap=my_cmap)
ax.plot

x= np.array([[2.5,2.5],[4,-1],[1,-4],[-3,1.25],[-2,-4],[1,5]])
y = np.array([1,1,1,0,0,0])

lr = LogisticRegression()

lr.fit(x, y, epochs = 1, refit=true, learning_rate=1)
plt.figure(figsize=(10,10 * 5))
for i in range (10):
    ax = plt.subplot(10, 1, i+1)
    plt.title("epoch {}".format(i+1))
    my_plot(x,y,lr,ax, i)
    lr.fit(x,y, epochs=1, refit=False, learning_rate=1)