Lie groups are without doubt the most important special class of differentiable manifolds. Lie groups are differentiable manifolds which are also groups and in which the group operations are smooth. Well-known examples include the general linear group, the unitary group, the orthogonal group, and the special linear group.

In this chapter we shall set the foundations for the study of Lie groups. Of central importance for Lie theory is the relationship between a Lie group and its Lie algebra of left invariant vector fields. We shall study the correspondence between subgroups and subalgebras and between homomorphisms of Lie groups and homomorphisms of their Lie algebras. We shall study the properties of the exponential mapping which is a generalization to arbitrary Lie groups of the exponentiation of matrices and which provides a key link between a Lie group and its Lie algebra. We shall investigate the adjoint representation, shall prove the closed subgroup theorem, and shall consider basic properties and examples of homogeneous manifolds. Along the way we shall derive many properties of the classical linear groups.

##### LIE GROUPS AND THEIR LIE ALGEBRAS

3.1 Definition A Lie group $G$ is a differentiable manifold which is also endowed with a group structure such that the map $G \times G \to G$ defined by $(\sigma, \tau) \mapsto \sigma\tau^{-1}$ is $C^\infty$.

Throughout this chapter, G and H will denote Lie groups, and we shall universally use e to denote the identity element of a Lie group.

### 3.2 Remarks

(a) Let $G$ be a Lie group. Then the map $\tau \mapsto \tau^{-1}$ is $C^\infty$ since it is the composition $\tau \mapsto (e, \tau) \mapsto \tau^{-1}$ of $C^\infty$ maps. Also, the map $(\sigma, \tau) \mapsto \sigma\tau$ of $G \times G \to G$ is $C^\infty$ since it is the composition $(\sigma, \tau) \mapsto (\sigma, \tau^{-1}) \mapsto \sigma\tau$ of $C^\infty$ maps.

(b) The identity component of a Lie group is itself a Lie group; and the components of a Lie group are mutually diffeomorphic.

(c) Since we have included second countability in the definition 1.4 of differentiable manifold, Lie groups for us will always be second countable. In particular, they can have at most countably many components. It should be observed, however, that if second countability is dropped from the definition of Lie group, then connected Lie groups (hence also those with countably many components) would still be second countable. We leave the proof of this as an exercise. You will need to use the fact that a connected Lie group is the union of powers of any neighborhood of its identity (see 3.18).

### 3.3 Examples of Lie Groups

(a) The Euclidean space  $ R^{*} $ is a Lie group under vector addition.

(b) The non-zero complex numbers  $ C^{*} $ form a Lie group under multiplication.

(c) The unit circle  $ S^{1} \subset C^{*} $ is a Lie group with the multiplication induced from  $ C^{*} $.

(d) The product $G \times H$ of two Lie groups is itself a Lie group with the product manifold structure and the direct product group structure; that is, $(\sigma_{1},\tau_{1})(\sigma_{2},\tau_{2}) = (\sigma_{1}\sigma_{2},\tau_{1}\tau_{2})$.

(e) The $n$-torus $T^{n}$ ($n$ an integer $>0$) is the Lie group which is the product of the Lie group $S^{1}$ with itself $n$ times.

(f) The manifold $Gl(n,\mathbb{R})$ of all $n\times n$ non-singular real matrices is a Lie group under matrix multiplication.

(g) The set of all super-triangular $n \times n$ real matrices (all entries below the diagonal are zero) is a Lie group under matrix multiplication.

(h) Let $\mathbb{R}^{*}$ denote the non-zero real numbers, and let $K$ be the product manifold $\mathbb{R}^{*} \times \mathbb{R}$. With a group structure on $K$ defined by

 $$ (s,t)(s_{1},t_{1})=(s s_{1}\;,\;s t_{1}+t), $$ 

K becomes a Lie group. This Lie group is the group of affine motions of  $ \mathbb{R} $, for if we identify the element  $ (s,t) $ of K with the affine motion  $ x \mapsto sx + t $, then the multiplication in K is composition of affine motions.

(i) Let $K$ be the product manifold $GI(n,\mathbb{R}) \times \mathbb{R}^n$. We define a group structure on $K$ by setting $(A,v)(A_1,v_1)=(AA_1,Av_1+v)$. With this group structure, $K$ becomes a Lie group. This Lie group is the group of affine motions of $\mathbb{R}^n$, for if we identify the element $(A,v)$ of $K$ with the affine motion $x \mapsto Ax + v$ of $\mathbb{R}^n$, then the multiplication in $K$ is composition of affine motions.

3.4 Definition A Lie algebra g over  $ \mathbb{R} $ is a real vector space g together with a bilinear operator [, ]:  $ g \times g \to g $ (called the bracket) such that for all x, y, z  $ \in $ g,

 $$ [x,y]=-[y,x]. $$ 

(anti-commutativity)

(b)

 $$ [[x,y],z]+[[y,z],x]+[[z,x],y]=0. $$ 

(Jacobi identity)

The importance of the concept of Lie algebra is that there is a special finite dimensional Lie algebra intimately associated with each Lie group, and that properties of the Lie group are reflected in properties of its Lie algebra. We shall see, for example, that the connected, simply connected Lie groups are completely determined (up to isomorphism) by their Lie algebras. The study of these Lie groups then reduces in large part to a study of their Lie algebras.

### 3.5 Examples of Lie Algebras

(a) The vector space of all smooth vector fields on the manifold M forms a Lie algebra under the Lie bracket operation on vector fields.

(b) Any vector space becomes a Lie algebra if all brackets are set equal to 0. Such a Lie algebra is called abelian.

(c) The vector space  $ \mathrm{gl}(n,\mathbb{R}) $ of all  $ n \times n $ real matrices forms a Lie algebra if we set

 $$ [A,B]=A B-B A. $$ 

(d) A 2-dimensional vector space with basis x, y becomes a Lie algebra if we set

 $$ [x,x]=[y,y]=0\qquad\mathrm{a n d}\qquad[x,y]=y,\quad\therefore\quad\forall x\in\mathcal{X}. $$ 

and extend bilinearly.

(e)  $ R^{3} $ with the bilinear operation  $ X \times Y $ of the vector cross product is a Lie algebra.

The proof that the above are Lie algebras is left to the reader as an exercise.

3.6 Definitions Let $\sigma \in G$. Left translation by $\sigma$ and right translation by $\sigma$ are respectively the diffeomorphisms $l_{\sigma}$ and $r_{\sigma}$ of $G$ defined by

 $$ \begin{aligned}{}&{{}l_{\sigma}(\tau)=\sigma\tau,}\\ {}&{{}r_{\sigma}(\tau)=\tau\sigma}\\ \end{aligned} $$ 

for all $\tau \in G$. If $V$ is a subset of $G$, we denote $r_e(V)$ and $l_e(V)$ by $V\sigma$ and $\sigma V$ respectively. A vector field $X$ (not assumed a priori to be smooth) on $G$ is called left invariant if for each $\sigma \in G$, $X$ is $l_e$-related to itself; that is,

 $$ d l_{e}\circ x=x\circ l_{e}. $$ 

The set of all left invariant vector fields on a Lie group G will be denoted by the corresponding lowercase German letter g.

3.7 Proposition Let G be a Lie group and g its set of left invariant vector fields.

(a) g is a real vector space, and the map $\alpha: \mathfrak{g} \to G_e$ defined by $\alpha(X) = X(e)$ is an isomorphism of g with the tangent space $G_e$ to G at the identity. Consequently, $\dim \mathfrak{g} = \dim G_e = \dim G$.

(c) The Lie bracket of two left invariant vector fields is itself a left invariant vector field.

(b) Left invariant vector fields are smooth.

(d) g forms a Lie algebra under the Lie bracket operation on vector fields.

PROOF That g is a real vector space and that $\alpha$ is linear is clear. $\alpha$ is injective, for if $\alpha(X) = \alpha(Y)$, then for each $\sigma \in G$

 $$ X(\sigma)=d l_{\sigma}\big(X(e)\big)=d l_{\sigma}\big(Y(e)\big)=Y(\sigma); $$ 

hence $X = Y$. Moreover, $\alpha$ is surjective; for if $x \in G_e$, we let $X(\sigma) = dl_\sigma(x)$ for each $\sigma \in G$. Then $\alpha(X) = x$, and $X$ is left invariant since

 $$ X(\tau\sigma)=d l_{\tau\sigma}(x)=d l_{\tau}d l_{\sigma}(x)=d l_{\tau}\big(X(\sigma)\big) $$ 

for all  $ \sigma $ and  $ \tau $ in G. This proves part (a).

For (b), let  $ X \in g $, and let  $ f \in C^\infty(G) $. We need only show that  $ X f \in C^\infty(G) $. Now,

 $$ X f(\sigma)=X_{\sigma}f=d l_{\sigma}(X_{e})f=X_{e}(f\circ l_{\sigma}). $$ 

Thus we need to show that $\sigma \mapsto X_e(f \circ l_\sigma)$ is a $C^\infty$ function on $G$. We do this by exhibiting this function as a suitable composition of $C^\infty$ maps. Let $\varphi: G \times G \to G$ denote group multiplication, $\varphi(\sigma, \tau) = \sigma\tau$. And let $i_\sigma^1$ and $i_\sigma^2$ be the maps of $G \to G \times G$ defined by

 $$ \begin{aligned}{}&{{}i_{e}{}^{1}(\tau)=(\tau,e),}\\ {}&{{}i_{o}{}^{2}(\tau)=(\sigma,\tau).}\\ \end{aligned} $$ 

Let $Y$ be any $C^\infty$ vector field on $G$ such that $Y(e) = X(e)$. Then $(0,Y)$ is a smooth vector field on $G \times G$, and $[(0,Y)(f \circ \varphi)] \circ i_e^1$ is a $C^\infty$ function on $G$. Using part (d) of Exercise 24, Chapter 1, we obtain

 $$ \begin{aligned}{[(0,Y)(f\circ\varphi)]\circ i_{e}^{1}(\sigma)}&{{}=(0,Y)_{(\sigma,e)}(f\circ\varphi)}\\ {}&{{}=0_{\sigma}(f\circ\varphi\circ i_{e}^{1})+Y_{e}(f\circ\varphi\circ i_{\sigma}^{2})}\\ {}&{{}=X_{e}(f\circ\varphi\circ i_{\sigma}^{2})=X_{e}(f\circ l_{\sigma}).}\\ \end{aligned} $$ 

Thus $\sigma \mapsto X_{e}(f \circ I_{\sigma})$ is a smooth function on $G$, which proves part (b).

Since, by (b), left invariant vector fields are smooth, their Lie brackets are defined. Now, if $X$ is $l_{\sigma}$-related to itself, and $Y$ is $l_{\sigma}$-related to itself, then according to 1.55, $[X,Y]$ is $l_{\sigma}$-related to $[X,Y]$. Thus the Lie bracket of two left invariant vector fields is again a left invariant vector field. Part (d) is now an immediate consequence of 1.45.

3.8 Definition We define the Lie algebra of the Lie group G to be the Lie algebra g of left invariant vector fields on G. Alternatively, we could take as the Lie algebra of G the tangent space  $ G_{s} $ at the identity with Lie algebra structure induced by requiring the vector space isomorphism 3.7(a) of g with  $ G_{s} $ to be an isomorphism of Lie algebras. It will be convenient at times to consider the Lie algebra from this alternate point of view. In particular, we shall see (3.10 and 3.37) that the Lie algebras of the classical groups admit particularly nice interpretations in terms of their tangent spaces at the identity.

3.9 Remarks on Vector Spaces as Manifolds In 1.5(b) we observe that any finite dimensional real vector space $V$ is, in a natural way, a differentiable manifold. Let $\{e_i\}$ be a basis of $V$, and let $\{r_i\}$ be the dual basis. Now let $p \in V$. Then there is a natural identification of the tangent space $V_p$, to $V$ at $p$ with $V$ itself, given by

 $$ \left.\Sigma a_{i}\frac{\partial}{\partial r_{i}}\right\vert_{p}\leftrightarrow\left.\Sigma a_{i}e_{i}.\right. $$ 

It is easily seen that this identification is independent of the basis chosen. We shall often make use of this identification in describing tangent vectors to a vector space as elements of the vector space itself. In particular, if $\sigma(t)$ is a smooth curve in $V$, then

 $$ \dot{\sigma}(t_{0})=\operatorname*{l i m}_{t\to t_{0}}\frac{\sigma(t)-\sigma(t_{0})}{t-t_{0}}. $$ 

### 3.10 Examples of Lie Groups and Their Lie Algebras

(a) The real line  $ \mathbb{R} $ is a Lie group under addition. The left invariant vector fields are simply the constant vector fields  $ \{\lambda(d/dr): \lambda \in \mathbb{R}\} $. The bracket of any two such vector fields is 0.

(b) The General Linear Group. The set  $ \mathrm{gl}(n, \mathbb{R}) $ of all  $ n \times n $ real matrices is a real vector space of dimension  $ n^2 $. Matrices are added and multiplied by scalars componentwise. As we have already remarked,  $ \mathrm{gl}(n, \mathbb{R}) $ becomes a Lie algebra if we set  $ [A, B] = AB - BA $.

The general linear group $GI(n,\mathbb{R})$ inherits its manifold structure as the open subset of $gl(n,\mathbb{R})$ where the determinant function does not vanish, and is a Lie group under matrix multiplication. Let $x_{i}$ be the global coordinate function on $gl(n,\mathbb{R})$ which assigns to each matrix

its $ijth$ entry. Then if $\sigma, \tau \in Gl(n, \mathbb{R})$, $x_{ij}(\sigma\tau^{-1})$ is a rational function of $\{x_{kl}(\sigma)\}$ and $\{x_{kl}(\tau)\}$ with non-zero denominator, which proves that the map $(\sigma, \tau) \to \sigma\tau^{-1}$ is $C^\infty$.

Now let $g$ be the Lie algebra of $GI(n,\mathbb{R})$. Let $\alpha: \mathrm{gl}(n,\mathbb{R})_e \to \mathrm{gl}(n,\mathbb{R})$ be the canonical identification of the tangent space to $\mathrm{gl}(n,\mathbb{R})$ at the identity matrix $e$ with $\mathrm{gl}(n,\mathbb{R})$ itself. Thus for $v \in \mathrm{gl}(n,\mathbb{R})_e$,

 $$ \alpha(v)_{i j}=v(x_{i j}). $$ 

Then since $Gl(n,\mathbb{R})_{e}=gl(n,\mathbb{R})_{e}$, we have a natural map $\beta\colon\mathfrak{g}\to\mathfrak{gl}(n,\mathbb{R})$ defined by

 $$ \beta(X)=\alpha\bigl(X(e)\bigr). $$ 

We claim that $\beta$ is a Lie algebra isomorphism, and in this way we consider $\mathrm{gl}(n,\mathbb{R})$ to be the Lie algebra of $Gl(n,\mathbb{R})$. $\beta$ is clearly a vector space isomorphism. We need only show that

 $$ \beta([X,Y])=[\beta(X),\beta(Y)] $$ 

whenever $X, Y \in \mathfrak{g}$. Now,

 $$ (x_{i j}\circ l_{\sigma})(\tau)=x_{i j}(\sigma\tau)=\sum_{k}x_{i k}(\sigma)x_{k j}(\tau). $$ 

Since Y is a left invariant vector field,

 $$ \begin{aligned}{\big(Y(x_{i j})\big)(\sigma)}&{{}={d}l_{e}(Y_{e})(x_{i j})=Y_{e}(x_{i j}\circ l_{\sigma})}\\ {}&{{}=\sum_{k}x_{i k}(\sigma)Y_{e}(x_{k j})=\sum_{k}x_{i k}(\sigma)\alpha(Y_{e})_{k j}}\\ {}&{{}=\sum_{k}x_{i k}(\sigma)\beta(Y)_{k j}.}\\ \end{aligned} $$ 

Using (5), we now compute the  $ ijth $ component of  $ \beta([X,Y]) $:

 $$ \begin{aligned}{\beta([X,Y])_{i j}}&{{}=[X,Y]_{\sigma}(x_{i j})=X_{\sigma}\big(Y(x_{i j})\big)-Y_{\sigma}\big(X(x_{i j})\big)}\\ {}&{{}=\sum_{k}\left\{X_{\sigma}(x_{i k})\beta(Y)_{k j}-Y_{\sigma}(x_{i k})\beta(X)_{k i}\right\}}\\ {}&{{}=\sum_{k}\left\{\beta(X)_{i k}\beta(Y)_{k j}-\beta(Y)_{i k}\beta(X)_{k j}\right\}}\\ {}&{{}=[\beta(X),\beta(Y)]_{i j}.}\\ \end{aligned} $$ 

Hence $\beta$ is a Lie algebra isomorphism.

(c) Let $V$ be an $n$-dimensional real vector space. Let $\mathrm{End}(V)$ denote the set of all linear operators on $V$ (the set of endomorphisms of $V$), and let $\mathrm{Aut}(V) \subset \mathrm{End}(V)$ denote the subset of non-singular operators (the automorphisms). $\mathrm{End}(V)$ is a real vector space of dimension $n^{2}$, and it becomes a Lie algebra if we set

 $$ [I_{1},I_{2}]=I_{1}\circ I_{2}-I_{2}\circ I_{1}. $$ 

(7)

A basis of $V$ determines a diffeomorphism of $\mathrm{End}(V)$ with $\mathrm{gl}(n, \mathbb{R})$ sending $\mathrm{Aut}(V)$ onto $GI(n, \mathbb{R})$. It follows that $\mathrm{Aut}(V)$ inherits a manifold structure as an open subset of $\mathrm{End}(V)$ and is a Lie group under composition. Under the natural identification of $\mathrm{End}(V)$ with $\mathrm{End}(V)_e = \mathrm{Aut}(V)_e$ (where $e$ denotes the identity transformation on $V$), $\mathrm{End}(V)$ inherits a Lie algebra structure from the Lie algebra of $\mathrm{Aut}(V)$. This induced Lie algebra structure is precisely the one described in (7).

(d) Let $\mathrm{gl}(n,\mathbb{C})$ denote the set of all $n\times n$ complex matrices, and let $G\mathrm{l}(n,\mathbb{C})\subset\mathrm{gl}(n,\mathbb{C})$ be the subset of non-singular ones. $G\mathrm{l}(n,\mathbb{C})$ is known as the complex general linear group. $\mathrm{gl}(n,\mathbb{C})$ is a $2n^{2}$-dimensional real vector space, with a basis consisting of the matrices $\delta_{ij}$ and $\sqrt{-1}\delta_{ij}(i,j=1,\ldots,n)$ where $\delta_{ij}$ is the matrix all of whose entries are zero except for a $1$ in the $ij$th spot; and $\mathrm{gl}(n,\mathbb{C})$ forms a Lie algebra if we set $[A,B]=AB-BA$. $G\mathrm{l}(n,\mathbb{C})$ inherits a manifold structure as an open subset of $\mathrm{gl}(n,\mathbb{C})$ and is a Lie group under matrix multiplication. With considerations entirely analogous to those in Example (b), one sees that the natural identification of the Lie algebra of $G\mathrm{l}(n,\mathbb{C})$ with $\mathrm{gl}(n,\mathbb{C})$ is a Lie algebra isomorphism. Thus we may consider $\mathrm{gl}(n,\mathbb{C})$ as the Lie algebra of $G\mathrm{l}(n,\mathbb{C})$.

(e) Similarly, in analogy with Example (c), if $V$ is a complex $n$-dimensional vector space, and if $\mathrm{End}(V)$ denotes the set of complex linear transformations of $V$, and $\mathrm{Aut}(V) \subset \mathrm{End}(V)$ denotes the non-singular ones, then $\mathrm{Aut}(V)$ is a $2n^{2}$-dimensional Lie group with Lie algebra $\mathrm{End}(V)$.

### 3.11 Definition A form  $ \omega $ on G is called left invariant if

 $$ \delta l_{a}\omega=\omega $$ 

for each $\sigma \in G$. As in the case of left invariant vector fields, it is not necessary to assume that left invariant forms are smooth, for smoothness is a consequence of the left invariance. We shall denote the vector space of left invariant $p$-forms on $G$ by $E_{l \operatorname{inv}}^{\bullet}(G)$, and we let

 $$ E_{l^{*}_{\mathrm{i n v}}}(G)=\sum_{p=0}^{\mathrm{d i m}G}E_{l\mathrm{i n v}}^{p}(G). $$ 

Left invariant 1-forms are also known as Maurer-Cartan forms.

The following proposition is the analog for left invariant forms of 3.7. The proofs are straightforward, and we leave them to the reader as an exercise.

### 3.12 Proposition

(a) Left invariant forms are smooth.

(b) $E^{*}_{1\mathrm{inv}}(G)$ is a subalgebra of the algebra $E^{*}(G)$ of all smooth forms on $G$, and the map $\omega \to \omega(e)$ is an algebra isomorphism of $E^{*}_{1\mathrm{inv}}(G)$ onto $\Lambda(G_e^*)$. In particular, this map gives a natural isomorphism of $E^1_{1\mathrm{inv}}(G)$ with $G_e^*$ and hence with $g^*$. (In this way we shall consider $E^1_{1\mathrm{inv}}(G)$ as the dual space of the Lie algebra of $G$.)

(c) If $\omega$ is a left invariant 1-form and $X$ a left invariant vector field, then $\omega(X)$ is a constant function on $G$, and this constant is precisely the effect $\omega$ has on $X$ when $\omega$ is considered as an element of the dual space of $g$ as in part (b). (We shall consider $\omega(X)$ either as a constant function on $G$ or as the corresponding real number, the particular choice depending on the context.)

(d) If  $ \omega \in E_{\ell_{\mathrm{inv}}}^{1}(G) $ and  $ X, Y \in \mathfrak{g} $, then it follows from 2.25(f) that

 $$ d\omega(X,Y)=-\omega[X,Y]. $$ 

(e) Let $\{X_{1}, \ldots, X_{d}\}$ be a basis of g with dual basis $\{\omega_{1}, \ldots, \omega_{d}\}$ for $E_{l\text{inv}}^{1}(G)$. Then there exist constants $c_{ijk}$ such that

 $$ [X_{i},X_{j}]=\sum_{k=1}^{d}c_{i j k}X_{k}. $$ 

(The $c_{ijk}$ are called the structural constants of $G$ with respect to the basis $\{X_{i}\}$ of g.) They satisfy

(3)

 $$ \begin{array}{c}{c_{i j k}+c_{j i k}=0,}\\ {\sum_{r}(c_{i j r}c_{r k s}+c_{j k r}c_{r i e}+c_{k i r}c_{r j e})=0.}\\ \end{array} $$ 

The exterior derivatives of the $\omega_{i}$ are given by the Maurer-Cartan equations

 $$ d\omega_{i}=\sum_{j<k}c_{j k i}\omega_{k}\wedge\omega_{j}. $$ 

##### HOMOMORPHISMS

3.13 Definitions A map $\varphi: G \to H$ is a (Lie group) homomorphism if $\varphi$ is both $C^\infty$ and a group homomorphism of the abstract groups. We call $\varphi$ an isomorphism if, in addition, $\varphi$ is a diffeomorphism. An isomorphism of a Lie group with itself is called an automorphism. If $H = \text{Aut}(V)$ for some vector space $V$, or if $H = \text{Gl}(n, \mathbb{C})$ or $\text{Gl}(n, \mathbb{R})$, then a homomorphism $\varphi: G \to H$ is called a representation of the Lie group $G$.

If $g$ and $b$ are Lie algebras, a map $\psi: g \to b$ is a (Lie algebra) homomorphism if it is linear and preserves brackets $(\psi[X,Y]=[\psi(X),\psi(Y)]$ for all $X,Y\in g)$. If, in addition, $\psi$ is 1:1 and onto, then $\psi$ is an isomorphism. An isomorphism of $g$ with itself is called an automorphism. If $b=\mathrm{End}(V)$ for some vector space $V$, or if $b=\mathrm{gl}(n,\mathbb{C})$ or $\mathrm{gl}(n,\mathbb{R})$, then a homomorphism $\psi: g \to b$ is called a representation of the Lie algebra $g$.

Let $\varphi: G \to H$ be a homomorphism. Then since $\varphi$ maps the identity of $G$ to the identity of $H$, the differential $d\varphi$ of $\varphi$ is a linear transformation of $G_e$ into $H_e$. By means of the natural identifications of the tangent spaces at the identities with the Lie algebras, this linear transformation $d\varphi$ of $G_e$ into $H_e$ induces a linear transformation of $g$ into $b$ which we shall denote also by $d\varphi$. Thus

 $$ d\varphi\colon{\mathfrak{g}}\to{\mathfrak{b}}, $$ 

where if $X \in g$, then $d\varphi(X)$ is the unique left invariant vector field on $H$ such that

 $$ d\varphi(X)(e)=d\varphi\bigl(X(e)\bigr). $$ 

3.14 Theorem Let G and H be Lie groups with Lie algebras g and h respectively, and let $\varphi: G \to H$ be a homomorphism. Then

(a) $X$ and $d\varphi(X)$ are $\varphi$-related for each $X\in\mathfrak{g}$.

(b)  $ d\varphi: \mathfrak{g} \to \mathfrak{h} $ is a Lie algebra homomorphism.

PROOF Let  $ \tilde{X} = d\varphi(X) $. Then  $ \tilde{X} $ and  $ X $ are  $ \varphi $-related. For since  $ \varphi $ is a homomorphism,  $ l_{\varphi(\sigma)} \circ \varphi = \varphi \circ l_{\sigma} $; hence

 $$ \begin{aligned}{\tilde{X}\big(\varphi(\sigma)\big)}&{{}=d l_{\varphi(\sigma)}\tilde{X}(e)=d l_{\varphi(\sigma)}d\varphi\big(X(e)\big)}\\ {}&{{}=d(l_{\varphi(\sigma)}\circ\varphi)X(e)=d(\varphi\circ l_{\sigma})X(e)=d\varphi\big(X(\sigma)\big).}\\ \end{aligned} $$ 

This proves part (a). Now let $X, Y \in \mathfrak{g}$. Then for part (b), we must show that

 $$ [\widetilde{X,Y}]=[\widetilde{X},\widetilde{Y}]. $$ 

By 1.55, [X,Y] is  $ \varphi $-related to the left invariant vector field  $ [\tilde{X},\tilde{Y}] $. In particular,

 $$ [\tilde{X},\tilde{Y}](e)=d\varphi\big([X,Y](e)\big). $$ 

But  $ [X,Y] $, by Definition 3.13(2), is the unique left invariant vector field on H whose value at the identity is  $ d\phi([X,Y](e)) $. Thus (2) holds, and the theorem is proved.

3.15 Effect of Homomorphisms on Left Invariant Forms Let  $ \varphi: G \to H $ be a homomorphism. Then  $ \delta\varphi $ pulls left invariant forms on H back to left invariant forms on G, since whenever  $ \omega $ is a left invariant form

on H,

 $$ \begin{aligned}{\delta I_{\sigma}\delta\varphi(\omega)}&{{}=\delta(\varphi\circ l_{\sigma})\omega=\delta(l_{\varphi(\sigma)}\circ\varphi)\omega}\\ {}&{{}=\delta\varphi\dot{\varrho}l_{\varphi(\sigma)}(\omega)=\delta\varphi(\omega).}\\ \end{aligned} $$ 

Moreover, the mapping $\delta\varphi\colon E_{\ell_{\mathrm{inv}}}^{\ell}(H)\to E_{\ell_{\mathrm{inv}}}^{\ell}(G)$, considered as a mapping of the dual space of $\mathfrak{h}$ to the dual space of $\mathfrak{g}$, is precisely the transpose of $d\varphi\colon\mathfrak{g}\to\mathfrak{h}$; that is,

 $$ \big(\delta\varphi(\omega)\big)(X)=\omega\big(d\varphi(X)\big)\qquad\big(\omega\in E_{l\operatorname{l n}\mathtt{v}}^{1}(H);\quad X\in\mathfrak{g}\big). $$ 

Recall that if $\{\omega_1, \ldots, \omega_d\}$ is a basis of $E_{\mathrm{inv}}^{t}(H)$, then there are structural constants $\{c_{ijk}\}$ (see 3.12(4)) such that

 $$ \bar{d}\omega_{i}=\sum_{j<k}c_{j k i}\omega_{k}\wedge\omega_{j}. $$ 

Thus since $d$ and $\delta\phi$ commute,

 $$ \bar{d}\big(\delta\varphi(\omega_{i})\big)=\sum_{j<k}c_{j k i}\;\delta\varphi(\omega_{k})\wedge\delta\varphi(\omega_{j}). $$ 

Now let $\pi_{1}$ and $\pi_{2}$ be the canonical projections of $G \times H$ onto $G$ and $H$ respectively. Then the ideal $\mathcal{J}$ of forms on $G \times H$ generated by the collection of independent 1-forms

 $$ \{\delta\pi_{1}\delta\varphi(\omega_{i})-\delta\pi_{2}(\omega_{i})\colon i=1,\ldots,d\} $$ 

is a differential ideal; for using (4), we obtain for each i,

 $$ \begin{aligned}{d\big(\delta\pi_{1}\delta\varphi(\omega_{i})}&{{}-\delta\pi_{\mathtt{z}}(\omega_{i})\big)}\\ {}&{{}=\sum_{j<k}c_{j k i}\big(\delta\pi_{1}\delta\varphi(\omega_{k})\wedge\delta\pi_{1}\delta\varphi(\omega_{j})-\delta\pi_{\mathtt{z}}(\omega_{k})\wedge\delta\pi_{\mathtt{z}}(\omega_{j})\big)}\\ {}&{{}=\sum_{j<k}c_{j k i}[\{\delta\pi_{1}\delta\varphi(\omega_{k})-\delta\pi_{\mathtt{z}}(\omega_{k})\}\wedge\delta\pi_{1}\delta\varphi(\omega_{j})}\\ {}&{{}\quad+\delta\pi_{\mathtt{z}}(\omega_{k})\wedge\{\delta\pi_{1}\delta\varphi(\omega_{j})-\delta\pi_{\mathtt{z}}(\omega_{j})\}],}\\ \end{aligned} $$ 

which belongs to the ideal $\mathcal{J}$. Moreover, observe that the 1-forms (5) generating the differential ideal $\mathcal{J}$ are themselves left invariant 1-forms on $G \times H$. This follows immediately from applying $\delta l_{(\sigma,\xi)}$ to the forms (5), where $(\sigma,\xi)\in G\times H$, and from using the fact that $\pi_1\circ l_{(\sigma,\xi)}=l_\sigma\circ\pi_1$ and $\pi_2\circ l_{(\sigma,\xi)}=l_\xi\circ\pi_2$. Note also that the basis $\{\omega_i\}$ of $E^1_{l_\mathrm{inv}}(H)$ is a basis of the 1-forms on $H$ in the sense of 2.33.

To carry out the above construction of a differential ideal on $G \times H$, it is sufficient to start simply with a homomorphism of the Lie algebras rather than a homomorphism of the Lie groups. Let $G$ and $H$ be Lie groups, and let $\psi: g \to h$ be a homomorphism of their Lie algebras. $\psi$ has a transpose $\psi^*: E_{l_{\text{inv}}}^1(H) \to E_{l_{\text{inv}}}^1(G)$, namely,

 $$ \big(\psi^{*}(\omega)\big)(X)=\omega\big(\psi(X)\big)\qquad\big(\omega\in E_{l\operatorname{i n v}}^{1}(H);X\in\mathfrak{g}\big). $$ 

Let $\{\omega_i\}$ be a basis of $E_{\ell,\mathbf{i}\mathbf{n}\mathbf{v}}^(H)$. Then we claim that the ideal $\mathcal{I}$ of forms on $G \times H$ generated by the collection of independent 1-forms

 $$ \{\delta\pi_{1}(\psi^{*}(\omega_{i}))-\delta\pi_{2}(\omega_{i})\colon i=1,\cdots,d\} $$ 

is a differential ideal. This follows from a computation similar to (6) together with the observation that

 $$ d\bigl(\psi^{*}(\omega_{i})\bigr)=\sum_{j<k}c_{j k i}\psi^{*}(\omega_{k})\wedge\psi^{*}(\omega_{j}). $$ 

To prove (9), it suffices to prove that both sides have the same effect on an arbitrary pair X, Y of left invariant vector fields on G:

 $$ \begin{aligned}{d\big(\psi^{*}(\omega_{i})\big)(X,Y)}&{{}=-\psi^{*}(\omega_{i})[X,Y]=-\omega_{i}[\psi(X),\psi(Y)]}\\ {}&{{}=d\omega_{i}\big(\psi(X),\psi(Y)\big)}\\ {}&{{}=\sum_{j<k}c_{j k i}\omega_{k}\wedge\omega_{j}\big(\psi(X),\psi(Y)\big)}\\ {}&{{}=\sum_{j<k}c_{j k i}\psi^{*}(\omega_{k})\wedge\psi^{*}(\omega_{j})(X,Y).}\\ \end{aligned} $$ 

Here the first and third equalities follow from 3.12(1). Finally, observe that, in this case also, the forms (8) are left invariant on  $ G \times H $.

We shall make use of these ideals on  $ G \times H $ in proving existence and uniqueness of homomorphisms in various situations.

3.16 Theorem Let G be connected, and let $\varphi$ and $\psi$ be homomorphisms of G into $H$ such that the Lie algebra homomorphisms $d\varphi$ and $d\psi$ of $\mathfrak{g}$ into $h$ are identical. Then $\varphi = \psi$.

PROOF Since  $ d\varphi = d\psi $, we have

 $$ \begin{array}{r}{\delta\varphi=\delta\psi\colon E_{l\mathrm{i n v}}^{1}(H)\to E_{l\mathrm{i n v}}^{1}(G).}\end{array} $$ 

Thus we have two $C^\infty$ maps $\varphi$ and $\psi$ of the connected manifold $G$ into $H$, both agreeing at $e\in G$, and both having the same effect of pulling back a basis of 1-forms from $H$. Thus since the ideal of forms on $G\times H$ generated by the 1-forms 3.15(5) is a differential ideal, it follows from 2.34(b) that $\varphi=\psi$.

##### LIE SUBGROUPS

3.17 Definitions $(H,\varphi)$ is a Lie subgroup of the Lie group $G$ if

(a) H is a Lie group;

(b)  $ (H,\varphi) $ is a submanifold of G;

(c)  $ \varphi\colon H \to G $ is a group homomorphism.

 $ (H,\varphi) $ is called a closed subgroup of G if, in addition,  $ \varphi(H) $ is a closed subset of G.

Let g be a Lie algebra. A subspace $\mathfrak{h} \subset \mathfrak{g}$ is a subalgebra if $[X, Y] \in \mathfrak{h}$ whenever $X, Y \in \mathfrak{h}$. A subalgebra $\mathfrak{h} \subseteq \mathfrak{g}$ clearly forms a Lie algebra under the bracket induced from $\mathfrak{g}$.

Let $(H,\varphi)$ be a Lie subgroup of $G$, and let $\mathfrak{h}$ and $g$ be their respective Lie algebras. Then $d\varphi$ gives an isomorphism of $\mathfrak{h}$ with the subalgebra $d\varphi(\mathfrak{h})$ of $g$.

Various theorems assert the existence of unique subgroups satisfying certain conditions, and as in the case of submanifolds (1.33 is pertinent), uniqueness needs a little explanation in view of our definition of subgroup. We will consider two subgroups $(H,\varphi)$ and $(H_{1},\varphi_{1})$ of $G$ equivalent if there exists a Lie group isomorphism $\alpha: H \to H_{1}$ such that $\varphi_{1} \circ \alpha = \varphi$. This is an equivalence relation on the Lie subgroups of $G$, and uniqueness for Lie subgroups means uniqueness up to this equivalence. As in the case of submanifolds (see 1.33), each equivalence class of Lie subgroups of $G$ has a unique representative of the form $(A,i)$, where $A$ is a subset of $G$ which is an abstract subgroup of $G$ and which has a manifold structure (not necessarily with the relative topology) making $A$ into a Lie group such that the inclusion $i: A \to G$ yields a submanifold and hence a Lie subgroup of $G$. When we wish to consider a subgroup of $G$ in this latter form (i.e. as an actual subset of $G$) we usually drop any reference to a mapping and speak simply of the Lie subgroup $A$ of $G$, the inclusion map being understood. Also, we usually identify the Lie algebra $a$ of $A$ with $di(a)$ and simply speak of the Lie algebra of $A$ as a subalgebra of the Lie algebra of $G$. In particular, we identify a left invariant vector field $X$ on $A$ with the left invariant vector field $di(X)$ on $G$ with which it is inclusion-related.

We are now going to prove one of the fundamental theorems of Lie group theory, which asserts that there is a 1:1 correspondence between connected Lie subgroups of a Lie group and subalgebras of its Lie algebra. But first, we will need the following proposition.

3.18 Proposition Let G be a connected Lie group, and let U be a neighborhood of e. Then

 $$ G=\bigcup_{n=1}^{\infty}U^{n} $$ 

where $U^{n}$ consists of all $n$-fold products of elements of $U$. (We say that $U$ generates $G$)

PROOF Let $V$ be an open subset of $U$ containing $e$ such that $V = V^{-1}$ (where $V^{-1} = \{\sigma^{-1}: \sigma \in V\}$). For example, $V = U \cap U^{-1}$ will do. Let

 $$ H=\bigcup_{n=1}^{\infty}V^{n}\subset\bigcup_{n=1}^{\infty}U^{n}. $$ 

Then $H$ is an abstract subgroup of $G$ and is an open subset of $G$ since $\sigma \in H$ implies $\sigma V \subset H$. Thus each coset mod $H$ is open in $G$. Now, $H$ is the complement in $G$ of the union of all the cosets mod $H$ different from $H$ itself. Therefore $H$ is also a closed subset of $G$. Since $G$ is connected, and $H$ is also non-empty, $H$ must be all of $G$. This together with (2) implies (1).

3.19 Theorem Let $G$ be a Lie group with $L_{ie}$ algebra $\mathfrak{g}$, and let $\widetilde{\mathfrak{h}} \subset \mathfrak{g}$ be a subalgebra. Then there is a unique connected $L_{ie}$ subgroup $(H, \varphi)$ of $G$ such that $d\varphi(\mathfrak{h}) = \widetilde{\mathfrak{h}}$.

PROOF We define a distribution D on G by setting

 $$ \mathcal{D}(\sigma)=\{X(\sigma)\colon X\in\tilde{\mathfrak{h}}\} $$ 

for each $\sigma \in G$. Let $\dim \widetilde{b} = d$. Then $\mathcal{D}$ is of dimension $d$. $\mathcal{D}$ is smooth since $\mathcal{D}$ is globally spanned by a basis $X_1, \ldots, X_d$ for $\widetilde{b}$. Moreover, $\mathcal{D}$ is involutive, since if $X$ and $Y$ are vector fields lying in $\mathcal{D}$, then there are $C^\infty$ functions $\{a_i\}$ and $\{b_i\}$ on $G$ such that $X = \sum a_i X_i$ and $Y = \sum b_i X_i$, and thus

 $$ [X,Y]=\sum_{i,j=1}^{d}\{a_{i}b_{j}[X_{i},X_{j}]+a_{i}X_{i}(b_{j})X_{j}-b_{j}X_{j}(a_{i})X_{i}\}, $$ 

which again is a vector field in D since b is a subalgebra of g.

Let $(H,\varphi)$ be a maximal connected integral manifold of $\mathcal{D}$ through $e$ (see 1.64). Let $\sigma\in\varphi(H)$. Since $\mathcal{D}$ is invariant under left translations, $(H,I_{\varphi^{-1}}\circ\varphi)$ is also an integral manifold of $\mathcal{D}$ through $e$. Thus by the maximality, $I_{\varphi^{-1}}\circ\varphi(H)\subset\varphi(H)$. Therefore if $\sigma\in\varphi(H)$ and $\tau\in\varphi(H)$, then also $\sigma^{-1}\tau\in\varphi(H)$. It follows that $\varphi(H)$ is an abstract subgroup of $G$. Thus we can induce a group structure on $H$ so that $\varphi:H\to G$ is a homomorphism of abstract groups. It remains only to check that $H$ is a Lie group, that is, the map $\alpha:H\times H\to H$ where $\alpha(\sigma,\tau)=\sigma\tau^{-1}$ is $C^\infty$. Now, the map $\beta:H\times H\to G$ sending $(\sigma,\tau)\mapsto\varphi(\sigma)\varphi(\tau)^{-1}$ is $C^\infty$, and we have the following commutative diagram:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//ffebdd2f-6528-4bab-9626-b1ae4d195e35/markdown_1/imgs/img_in_image_box_353_929_594_1061.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2F5579a5192fcc53383e627fb14132deec748a33a7dd6e5b90ef21520b16d92bbb" alt="Image" width="24%" /></div>

Since $(H,\varphi)$ is an integral manifold of an involutive distribution on $G$, it follows from 1.62 that $\alpha$ is $C^\infty$. Thus $(H,\varphi)$ is a Lie subgroup of $G$; and if $\mathfrak{h}$ is the Lie algebra of $H$, clearly $d\varphi(\mathfrak{h})=\widetilde{\mathfrak{h}}$.

For uniqueness, let $(K,\psi)$ be another connected Lie subgroup of $G$ with $d\psi(\mathfrak{f})=\widetilde{\mathfrak{h}}$. Then $(K,\psi)$ must also be an integral manifold of $\mathcal{D}$ through $e$. By the maximality of $(H,\varphi)$, $\psi(K)\subset\varphi(H)$, and there is uniquely determined a map $\eta$ such that $\varphi\circ\eta=\psi$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//ffebdd2f-6528-4bab-9626-b1ae4d195e35/markdown_2/imgs/img_in_image_box_399_221_592_346.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A14Z%2F-1%2F%2Ffa10b9d31e6cc1b49acfdd65e35b8e6718be5acabab8c05b076e59997080172a" alt="Image" width="20%" /></div>

$\eta$ is smooth by 1.62, and consequently is an injective Lie group homomorphism. Moreover, $\eta$ is everywhere non-singular; in particular, $\eta$ is a diffeomorphism on a neighborhood of the identity, and therefore is surjective by 3.18. Thus $\eta$ is a Lie group isomorphism, and the subgroups $(K,\psi)$ and $(H,\varphi)$ are equivalent. This proves uniqueness.

Corollary (a) There is a 1:1 correspondence between connected Lie subgroups of a Lie group and subalgebras of its Lie algebra.

Corollary (b) Let $(H,\varphi)$ be a Lie subgroup of $G$. Then if $\tilde{H}$ is a component of $H$, $(\tilde{H},\varphi|\tilde{H})$ is a maximal connected integral manifold of the involutive distribution on $G$ determined by the subalgebra $d\varphi(h)$ of $g$.

We can restate the content of part of the proof of Theorem 3.19 in terms of differential ideals on G as follows (cf. Exercise 6):

Corollary (c) Suppose that the ideal $\mathcal{I}$ generated by a collection $\{\omega_1, \ldots, \omega_{c-d}\}$ of independent left invariant 1-forms on a Lie group $G^c$ is a differential ideal. Then the maximal connected integral manifold $I^a$ of $\mathcal{I}$ through $e \in G$ is a Lie subgroup of $G$.

The following theorem should be compared with the situation for submanifolds (see 1.33).

3.20 Theorem If an abstract subgroup $A$ of a Lie group $G$ has a manifold structure (that is, a second countable locally Euclidean topology together with a differentiable structure) which makes $(A,i)$ into a submanifold of $G$, where $i$ is the inclusion map, then it has a unique such manifold structure, and in this manifold structure, $A$ is a Lie group, and hence $(A,i)$ is a Lie subgroup of $G$.

PROOF We show first that in any such manifold structure, $A$ is a Lie group. Let $\mathcal{D}$ be the distribution on $G$ determined by left translations of the tangent space to $A$ at the identity. We claim that $(A,i)$ is an integral manifold of $\mathcal{D}$ through the identity $e\in G$.

We caution that this is not evident and that its proof requires a little care. The problem is that if $\gamma(t)$ is a smooth curve in $A$, and if $\sigma$ lies in $A$, then $I_{\sigma} \circ \gamma(t)$ is a smooth curve in $G$ which lies in $A$ but apriori may no longer be smooth in $A$. Thus it could be that there are elements of $\mathcal{D}(\sigma)$ which are not tangent vectors to $A$. We must show that this cannot occur. Let $\dim A = k$. If for some $\sigma \in A$ the tangent space $A_{\sigma}$ is not contained in $\mathcal{D}(\sigma)$, then we can find $k + 1$ curves which are smooth in $G$, lie in $A$, and have independent tangent vectors at $\sigma$. Translating to the identity, we have curves $\gamma_{1}(t), \ldots, \gamma_{k+1}(t)$ which are smooth in $G$, lie in $A$, pass through $e$ at $t = 0$, and have independent tangent vectors there. Notice that this is not yet a contradiction. For example, there are two smooth curves in the plane $\mathbb{R}^{k}$ with independent tangent vectors at the origin and lying in the one-dimensional figure-8 submanifold (see 1.31). Now consider the map

 $$ (t_{1},\ldots,t_{k+1})\mapsto\gamma_{1}(t_{1})\cdot\cdot\cdot\gamma_{k+1}(t_{k+1}). $$ 

This map is non-singular at the origin, thus is a diffeomorphism of a neighborhood of the origin in $\mathbb{R}^{k+1}$ into $G$, and has its image contained in $A$ since the individual curves $\gamma_t$ lie in $A$, and $A$ is a subgroup. The map (5) can be extended to a diffeomorphism of a neighborhood of the origin in $\mathbb{R}^*$ with a neighborhood $U$ of the identity in $G$, where $n = \dim G$. Composing the inverse of this diffeomorphism with the inclusion $I: A \to G$, we obtain a $C^\infty$ immersion of the open submanifold $U \cap A$ of $A$ into $\mathbb{R}^*$ with image containing an open set in $\mathbb{R}^{k+1} \subset \mathbb{R}^*$. This now contradicts the fact that $A$ is second countable and has dimension $k$. (See Exercise 6, Chapter 1.) Thus $A_e = D(\sigma)$ for each $\sigma \in A$ and consequently $(A, i)$ is an integral manifold of $\mathcal{D}$.

It follows that for any $\sigma\in G$, $(A,I_{e})$ is an integral manifold of $\mathcal{D}$ through $\sigma$. Thus by 1.59, $\mathcal{D}$ is an involutive distribution; and now it follows from an argument as in 3.19(3) that the map $(\sigma,\tau)\to\sigma\tau^{-1}$ of $A\times A\to A$ is $C^{\infty}$, which proves that $A$ is a Lie group. Now suppose that we have two manifold structures on $A$ for which $(A,i)$ is a submanifold. Denote $A$ with these manifold structures by $A_{1}$ and $A_{2}$ respectively. Then $(A_{1},i)$ and $(A_{2},i)$ are both integral manifolds of involutive distributions on $G$; hence 1.62 applied to the commutative diagram

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//ffebdd2f-6528-4bab-9626-b1ae4d195e35/markdown_3/imgs/img_in_image_box_365_968_576_1111.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A14Z%2F-1%2F%2F900ea5643cf10391db1b5dc8d21d62d53722b0ad471a3371d6c05bfb8a173dab" alt="Image" width="21%" /></div>

implies that the identity map id: $A_{1} \to A_{2}$ is a diffeomorphism. Thus there is a unique such manifold structure on $A$.

Hence if a subset of a Lie group can be made into a Lie subgroup under the inclusion map, it can be made so in one and only one way—the group structure, topology, and differentiable structure are uniquely determined. Consequently, it is unambiguous to assert that a subset A of a Lie group G is a Lie subgroup of G. This means that A is an abstract subgroup of G and has a manifold structure (and hence a unique one) making A into a Lie group and  $ (A,i) $ into a Lie subgroup of G.

We are now in a position to describe exactly in which situation a Lie subgroup $A \subseteq G$ has the relative topology.

3.21 Theorem Let $(H^{a},\varphi)$ be a Lie subgroup of $G^{c}$. Then $\varphi$ is an imbedding (that is, $\varphi$ is a homeomorphism of $H$ with $\varphi(H)$ in the relative topology) if and only if $(H,\varphi)$ is a closed subgroup of $G$ (that is, $\varphi(H)$ is closed in $G$).

PROOF Assume that $\varphi(H)$ is closed in $G$. It suffices to prove that there is some non-empty open set $V \subset H$ such that $\varphi \mid V$ is a homeomorphism of $V$ into $\varphi(H)$ where $\varphi(H)$ has the relative topology. For then it follows from the fact that $\varphi$ commutes with left translations $(\varphi \circ I_e) = I_{\varphi(e)} \circ \varphi)$ that $\varphi$ is an imbedding on all of $H$. By 3.19, Corollary (b), and by 1.60, there exists a cubic-centered coordinate system $(U, \tau)$ about $e \in G$ such that $\varphi(H) \cap U$ consists of a union (at most countable) of slices of the form

 $$ \tau_{i}=\mathtt{c o n s t a n t}\qquad\mathrm{f o r~a l l~}i\in\{d+1,\ldots,c\}, $$ 

including at least the slice through $e$. Let $C$ be a closed subset of $U$ containing $e$ whose image under $\tau$ is a cube, and let $S$ be the slice of $C$ given by

 $$ \tau_{1}=0,\ldots,\tau_{d}=0. $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//343ed485-5e7c-4aa2-bb5c-9fdcbe4c76d3/markdown_0/imgs/img_in_image_box_343_810_737_1070.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A26Z%2F-1%2F%2F63c6189a67f6512423681626fc5c196ea04e43dc63042e7b5f1771fc9cb92c51" alt="Image" width="41%" /></div>

Then  $ \tau(\varphi(H) \cap S) $ is a non-empty, closed, countable subset of  $ \mathbb{R}^{c-d} $. Now, any closed countable subset of Euclidean space must have an isolated point. Otherwise, such a set with the induced metric would be a

complete metric space representable as a countable union of nowhere dense sets, which is impossible according to the Baire category theorem [27]. Thus there is an isolated slice, call it $S_0$, among the collection of slices $\varphi(H) \cap U$; and thus $\varphi^{-1}(S_0)$ is an open subset of $H$ on which $\varphi$ gives an imbedding into $\varphi(H)$.

Conversely, suppose that $\varphi$ is an imbedding. Let $\{\sigma_i\}$ be a sequence of points in $\varphi(H)$ converging to the point $\sigma \in G$. Since $\varphi$ is an imbedding, there exists a cubic coordinate system $(U, \tau)$ about the identity $e \in G$ such that $\varphi(H) \cap U$ consists of a single slice—call it $S$. Choose neighborhoods $V \subset W \subset U$ of the identity, cubic relative to $\tau$, so that $V^{-1}V \subset W \subset U$. Since $\sigma_i \to \sigma$, there is an $N$ sufficiently large so that $\sigma_n \in \sigma V$ for $n \geq N$. Therefore $\sigma_N^{-1} \sigma_n \in \overline{W}$ for $n \geq N$. Also $\sigma_N^{-1} \sigma_n \in \varphi(H)$. Thus $\sigma_N^{-1} \sigma_n \in S \cap \overline{W}$ and converges to $\sigma_N^{-1} \sigma$ which therefore must also lie in $S \cap \overline{W}$. Therefore $\sigma_N^{-1} \sigma \in \varphi(H)$. Hence $\sigma \in \varphi(H)$, and thus $\varphi(H)$ is closed.

##### COVERINGS

We shall assume that the reader has some familiarity with the notions of homotopy, fundamental group, simple connectivity, and covering space. In Theorem 3.23 we state three of the fundamental facts on covering spaces which we shall need. The proofs are sketched in Exercise 7 at the end of this chapter. Details of the proofs and additional facts on covering spaces may be found, for example, in [26] or [28].

3.22 Definition Before stating Theorem 3.23, we recall a few definitions and establish some notation. We let  $ \pi_1(X, x_0) $ denote the fundamental group of the topological space  $ X $ with base point  $ x_0 \in X $. We let  $ \pi \colon (X, x_0) \to (Y, y_0) $ denote a mapping of the topological space  $ X $ into the topological space  $ Y $ sending the base point  $ x_0 $ in  $ X $ to the base point  $ y_0 $ in  $ Y $, and we denote the corresponding induced homomorphism of the fundamental groups by  $ \pi_* \colon \pi_1(X, x_0) \to \pi_1(Y, y_0) $.

We shall assume connectedness in the definition of "simply connected." That is, we shall assume a simply connected space X to be a connected topological space whose fundamental group is trivial.

A continuous surjection $\pi: X \to Y$ is called a covering if $X$ is a connected, locally pathwise connected (each neighborhood of a point contains a pathwise connected neighborhood of that point) topological space, and if each point $y \in Y$ has a neighborhood $V$ whose inverse image under $\pi$ is a disjoint union of open sets in $X$ each homeomorphic with $V$ under $\pi$. Such neighborhoods $V$ in $Y$ are called evenly covered. If $\pi: X \to Y$ is a covering, then $Y$ is called the base of the covering, and $X$ is called the covering space.

A topological space Y is called semi-locally 1-connected if each point $y \in Y$ has a neighborhood U such that each loop based at $y$ and lying in U is homotopic in Y, through loops based at $y$, to the constant loop.

### 3.23 Theorem

(a) Let $\pi: (X, x_0) \to (Y, y_0)$ be a covering. Let $Z$ be a pathwise connected and locally pathwise connected topological space, and let $\alpha: (Z, z_0) \to (Y, y_0)$ be a continuous map such that $\alpha_*(\pi_1(Z, z_0)) \subset \pi_*(\pi_1(X, x_0))$. Then there exists a unique continuous map $\tilde{\alpha}: (Z, z_0) \to (X, x_0)$ such that $\pi \circ \tilde{\alpha} = \alpha$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//343ed485-5e7c-4aa2-bb5c-9fdcbe4c76d3/markdown_2/imgs/img_in_image_box_353_266_620_408.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A28Z%2F-1%2F%2Fda85c451b29eee72a6a95b0cc50e4950995d64ddfd7f7021a6dca8ff682511e8" alt="Image" width="28%" /></div>

(b) If X is a pathwise connected, locally pathwise connected, and semilocally 1-connected topological space, then X has a simply connected covering space.

(c) If  $ \pi: X \to Y $ is a covering and Y is simply connected, then  $ \pi $ is a homeomorphism.

3.24 Simply Connected Covering Group Let $\pi: \overrightarrow{M} \to M$ be a covering of a differentiable manifold $M$. Then $\overrightarrow{M}$ is automatically a locally Euclidean, second countable (cf. Exercise 8) Hausdorff space, and there is a unique differentiable structure on $\overrightarrow{M}$ for which the covering map $\pi$ is $C^\infty$ and non-singular. This differentiable structure is obtained simply by requiring that the local homeomorphisms obtained from $\pi$ over evenly covered open sets be diffeomorphisms.

Now let $G$ be a connected Lie group. By $3.23(b)$, $G$ has a covering $\pi: \tilde{G} \to G$ with $\tilde{G}$ simply connected. As we have observed, $\tilde{G}$ has a unique differentiable structure for which $\pi$ is $C^\infty$ and non-singular. We shall now show that a group structure can be induced in $\tilde{G}$ making $\tilde{G}$ into a Lie group and making $\pi$ into a Lie group homomorphism. Consider the map $\alpha: \tilde{G} \times \tilde{G} \to G$ such that $\alpha(\tilde{\sigma}, \tilde{\tau}) = \pi(\tilde{\sigma}) \pi(\tilde{\tau})^{-1}$. Choose $\tilde{\varepsilon} \in \pi^{-1}(e)$. Since $\tilde{G} \times \tilde{G}$ is simply connected, it follows from $3.23(a)$ that a unique mapping $\tilde{\alpha}: \tilde{G} \times \tilde{G} \to \tilde{G}$ exists such that $\pi \circ \tilde{\alpha} = \alpha$ and such that $\tilde{\alpha}(\tilde{\varepsilon}, \tilde{\varepsilon}) = \tilde{\varepsilon}$. For $\tilde{\sigma}$ and $\tilde{\tau}$ in $\tilde{G}$ we define

 $$ \tilde{\tau}^{-1}=\tilde{\alpha}(\tilde{e},\tilde{\tau}),\quad\tilde{\sigma}\tilde{\tau}=\tilde{\alpha}(\tilde{\sigma},\tilde{\tau}^{-1}). $$ 

It follows easily from applications of the uniqueness part of 3.23(a) that $\tilde{\sigma}\tilde{e}=\tilde{e}\tilde{\sigma}=\tilde{\sigma}$, for the maps $\tilde{\sigma}\mapsto\tilde{\sigma}\tilde{e}$, $\tilde{\sigma}\mapsto\tilde{e}\tilde{\sigma}$, and $\tilde{\sigma}\mapsto\tilde{\sigma}$ of $\tilde{G}\to\tilde{G}$ all make the following diagram commute, and they all send $\tilde{e}$ to $\tilde{e}$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//343ed485-5e7c-4aa2-bb5c-9fdcbe4c76d3/markdown_2/imgs/img_in_image_box_377_1064_567_1211.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A29Z%2F-1%2F%2Fabcae376d155f555a4f06c1037dd33ff6a2ff002b327be87f46a58564b18fb96" alt="Image" width="19%" /></div>

Thus since $\tilde{G}$ is simply connected, it follows from the uniqueness in 3.23(a) that these maps are all identical. Similarly, if follows that $\tilde{\sigma}\tilde{\sigma}^{-1}=\tilde{\sigma}^{-1}\tilde{\sigma}=\tilde{\varepsilon}$, and that $(\tilde{\sigma}\tilde{\tau})\tilde{\gamma}=\tilde{\sigma}(\tilde{\tau}\tilde{\gamma})$ for all $\tilde{\sigma},\tilde{\tau},\tilde{\gamma}\in\tilde{G}$, Thus (1) makes $\tilde{G}$ into an abstract group; and since $\tilde{\alpha}$ is smooth, $\tilde{G}$ is a Lie group. Also, (1) implies that $\pi(\tilde{\tau}^{-1})=\pi(\tilde{\tau})^{-1}$ and that $\pi(\tilde{\sigma}\tilde{\tau})=\pi(\tilde{\sigma})\pi(\tilde{\tau})$; hence $\pi:\tilde{G}\to G$ is a Lie group homomorphism. Thus we have proved the following.

3.25 Theorem Each connected Lie group has a simply connected covering space which is itself a Lie group such that the covering map is a Lie group homomorphism.

3.26 Proposition Let G and H be connected Lie groups, and let $\varphi: G \to H$ be a homomorphism. Then $\varphi$ is a covering map if and only if $d\varphi: G_s \to H_s$ is an isomorphism.

PROOF Suppose first that $\varphi$ is a covering. Then $d\varphi \mid G_{\epsilon}$ must be injective. Otherwise, since $\varphi$ is a homomorphism, $d\varphi$ would have a nontrivial kernel at each point of $G$, and these kernels would form an involutive distribution on $G$, whose integral manifolds are collapsed to points under $\varphi$. Thus $\varphi$ would nowhere be locally one-to-one, contradicting the covering property. $d\varphi \mid G_{\epsilon}$ must also be surjective, for otherwise $(G,\varphi)$ would locally be a proper submanifold of $H$, again contradicting the local homeomorphism property of a covering. Thus $d\varphi:G_{\epsilon}\to H_{\epsilon}$ is an isomorphism.

Conversely, suppose that $d\varphi:G_{s}\to H_{s}$ is an isomorphism. Then $\varphi$ is everywhere a local diffeomorphism. Thus, by 3.18, $\varphi$ maps $G$ onto $H$ since $\varphi$ is a homomorphism and since $\varphi(G)$ contains a neighborhood of the identity in the connected Lie group $H$. $G$ certainly is pathwise and locally pathwise connected, so to prove that $\varphi$ is a covering map, it only remains to show that each point of $H$ is contained in an evenly covered neighborhood. Let

 $$ D=\ker\varphi=\varphi^{-1}(e). $$ 

Then since $\varphi$ is a local diffeomorphism, $D$ is a discrete normal subgroup of $G$, where “discrete” means that if $\sigma \in D$, then there is an open set $V$ in $G$ such that $V \cap D = \sigma$. Since $(\sigma, \tau) \mapsto \sigma^{-1} \tau$ is a continuous (in fact $C^\infty$) map of $G \times G \to G$, there exists a neighborhood $V$ of $e$ in $G$ such that

 $$ (V^{-1}V)\cap D=e. $$ 

We claim that $\varphi(V)$ is a neighborhood of $e$ in $H$, evenly covered by $\varphi$. First, $\varphi\big|V$ is $1:1$, since if $\sigma,\tau\in V$ and $\varphi(\sigma)=\varphi(\tau)$, then $\varphi(\sigma^{-1}\tau)=e$, whence $\sigma^{-1}\tau=e$ by (2), and thus $\sigma=\tau$. Moreover, $d\varphi$ is an isomorphism at each point of $G$. Thus $\varphi\big|V$ is a diffeomorphism of $V$ with the open neighborhood $\varphi(V)$ of $e$ in $H$. Now, we claim that

 $$ \varphi^{-1}\bigl(\varphi(V)\bigr)=\bigcup_{\theta\in D}V\theta. $$ 

The inclusion $\supset$ is obvious. To prove $\subset$, suppose that $\varphi(\sigma) \in \varphi(V)$. Then there exists $\tau \in V$ such that $\varphi(\tau) = \varphi(\sigma)$. Hence $\tau^{-1}\sigma \in D$ and $\sigma \in V\tau^{-1}\sigma$, proving (3). Finally, $V\theta_1 \cap V\theta_2 = \varnothing$ if $\theta_1 \neq \theta_2 \in D$, for if $\sigma \in V\theta_1 \cap V\theta_2$ then $\sigma = \tau\theta_1 = \eta\theta_2$ for some $\tau$, $\eta \in V$. Then $\tau^{-1}\eta \in D$ and $\tau^{-1}\eta \in V^{-1}V$; thus, by (2), $\tau = \eta$, which implies that $\theta_1 = \theta_2$. Thus $\varphi(V)$ is an evenly covered neighborhood of $e \in H$. It follows that $\varphi(\sigma V)$ is an open neighborhood of $\varphi(\sigma)$ in $H$, evenly covered by the disjoint union of the open sets $\sigma V\theta$ for $\theta \in D$. Thus $\varphi$ is a covering.

##### SIMPLY CONNECTED LIE GROUPS

3.27 Theorem Let G and H be Lie groups with Lie algebras g and h respectively and with G simply connected. Let $\psi: \mathfrak{g} \to \mathfrak{h}$ be a homomorphism. Then there exists a unique homomorphism $\psi: G \to H$ such that $d\varphi = \psi$.

PROOF Uniqueness was proved in 3.16.

Let $\{\omega_i\}$ be a basis of the left invariant 1-forms on $H$, and let $\psi^*$ be the transpose of $\psi$ (see 3.15(7)). Then according to 3.15, the 1-forms

 $$ \{\delta\pi_{1}\big(\psi^{*}(\omega_{i})\big)-\delta\pi_{2}(\omega_{i})\} $$ 

on $G \times H$ (where $\pi_1$ and $\pi_2$ are the canonical projections of $G \times H$ onto $G$ and $H$ respectively) are left invariant, and the ideal $\mathcal{J}$ which they generate is a differential ideal. Thus by 3.19, Corollary (c), the maximal connected integral manifold $I$ of $\mathcal{J}$ through $(e,e) \in G \times H$ is a Lie subgroup of $G \times H$ with dimension equal to the dimension of $G$. Now, we know from 2.33 that $(\pi_1 \mid I): I \to G$ is non-singular, and therefore by 3.26 is a covering homomorphism. $G$ was assumed to be simply connected; hence by 3.23(c) and the inverse function theorem, $\pi_1 \mid I: I \to G$ is an isomorphism. We define $\varphi: G \to H$ by setting

 $$ \varphi=\pi_{2}\circ(\pi_{1}\mid I)^{-1}. $$ 

Then $\varphi$ is a Lie group homomorphism, and according to 2.33(6),

 $$ \delta\varphi(\omega_{i})=\varphi^{*}(\omega_{i}). $$ 

Thus $d\varphi=\varphi$, and the theorem is proved.

Corollary If simply connected Lie groups G and H have isomorphic Lie algebras, then G and H are isomorphic.

There is a theorem [12, p. 199] due to Ado, which we will not prove, that every Lie algebra has a faithful (1:1) representation in $\mathrm{gl}(n,\mathbb{R})$ for some $n$. As a consequence, if $g$ is a Lie algebra, then there is a Lie group, in particular a simply connected one, with Lie algebra $g$. In view of this we have:

3.28 Theorem There is a one-to-one correspondence between isomorphism classes of Lie algebras and isomorphism classes of simply connected Lie groups.

##### EXPONENTIAL MAP

3.29 Definition A homomorphism $\varphi: \mathbb{R} \to G$ is called a 1-parameter subgroup of $G$.

3.30 Definition Let $G$ be a Lie group, and let $g$ be its Lie algebra. Let $X \in g$. Then

 $$ \lambda\frac{d}{d r}\mapsto\lambda X $$ 

is a homomorphism of the Lie algebra of  $ \mathbb{R} $ into g. Since the real line is simply connected, there exists, by 3.27, a unique 1-parameter subgroup

 $$ \mathtt{e x p}_{\mathtt{X}}\colon\mathbb{R}\to G $$ 

such that

 $$ \begin{array}{r}{d\exp_{\boldsymbol{X}}\Big(\lambda\frac{d}{d r}\Big)=\lambda\boldsymbol{X}.}\end{array} $$ 

In other words, $t \mapsto \exp_{X}(t)$ is the unique 1-parameter subgroup of $G$ whose tangent vector at $0$ is $X(e)$. We define the exponential map

 $$ \mathbf{e x p}\colon\mathfrak{g}\to G $$ 

 $$ \operatorname{e x p}(X)=\operatorname{e x p}_{X}(1). $$ 

by setting

The reason for this terminology will become apparent in 3.35(13), where we show that the exponential map for the general linear group is actually given by exponentiation of matrices.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//008e99d6-8a1d-4188-b841-b6c361e3463a/markdown_1/imgs/img_in_image_box_238_851_657_1180.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A28Z%2F-1%2F%2Fa6f8281712960fc665796099a47d45cd3b98b8fcc49721d945467336be807227" alt="Image" width="42%" /></div>

3.31 Theorem Let $X$ belong to the Lie algebra $g$ of the Lie group $G$. Then

(a)  $ \exp(tX) = \exp_X(t) $ for each  $ t \in \mathbb{R} $.

 $$ \quad\quad(b)\quad\operatorname{e x p}(t_{1}+t_{2})X=(\operatorname{e x p}t_{1}X)(\operatorname{e x p}t_{2}X)\qquad{f o r\quad a l l}t_{1},t_{2}\in\mathbb{R}. $$ 

(c)  $ \exp(-tX) = (\exp tX)^{-1} $ for each  $ t \in \mathbb{R} $.

(d) $\exp: \mathfrak{g} \to G$ is $C^{\infty}$ and $d \exp: \mathfrak{g}_{0} \to G_{*}$ is the identity map (with the usual identifications), so $\exp$ gives a diffeomorphism of a neighborhood of 0 in $\mathfrak{g}$ onto a neighborhood of $e$ in $G$.

(e) $l_{e}\circ\exp_{X}$ is the unique integral curve of $X$ which takes the value $\sigma$ at 0. As a particular consequence, left invariant vector fields are always complete.

(f) The 1-parameter group of diffeomorphisms $X_{t}$ associated with the left invariant vector field $X$ is given by

 $$ X_{t}=r_{\mathrm{e x p}_{X}}(t). $$ 

PROOF By 3.14, $(d/dr)$ and $d\exp_X(d/dr)$, which is $X$, are $\exp_X$ related. Thus $\exp_X$ is an integral curve of $X$ and is the unique one for which $\exp_X(0) = e$. Since $X$ is left invariant, $I_\sigma^\circ \circ \exp_X$ is also an integral curve of $X$ and is the unique one taking the value $\sigma$ at 0. Thus part (e) is proved; and (f) is an immediate consequence of (e). Now define $\mathbf{maps} \varphi$ and $\psi$ of $\mathbb{R}$ into $G$ by setting

 $$ \psi(t)=\exp_{s\mathbf{x}}(t)\qquad\mathrm{a n d}\qquad\varphi(t)=\exp_{x}(s t) $$ 

where $s \in \mathbb{R}$. We have observed that $\psi$ is the unique integral curve of $sX$ such that $\psi(0) = e$. Now,

 $$ d_{\Phi}\left(\frac{d}{d r}\bigg\vert_{t}\right)=d\operatorname{e x p}_{X}\left(s\frac{d}{d r}\bigg\vert_{s t}\right)=s X\big\vert_{\operatorname{e x p}_{X}(s t)}. $$ 

Thus $\varphi$ also is an integral curve of $sX$ such that $\varphi(0)=e$. By the uniqueness (1.48(c)) of integral curves, $\varphi=\psi$. Thus

 $$ \operatorname{e x p}_{s X}(t)=\operatorname{e x p}_{X}(s t)\qquad(s,\;t\in\mathbb{R}\;;\;X\in\mathfrak{g}). $$ 

Setting $t=1$ and changing $s$ to $t$, we obtain part (a). Since $\exp_X$ is a homomorphism of $\mathbb{R}$ into $G$, parts (b) and (c) follow immediately from (a). For part (d), we define a vector field $V$ on $G\times g$ by setting

 $$ V(\sigma,X)=(X(\sigma),0)\in G_{\sigma}\oplus\mathfrak{g}_{X}. $$ 

Then $V$ is a smooth vector field, and according to part (e), the integral curve of $V$ through $(\sigma,X)$ is

 $$ \iota\quad\mapsto\quad(\sigma\exp\iota X,X), $$ 

or in other words, the local 1-parameter group of transformations associated with the vector field V is given by

 $$ V_{t}(\sigma,X)=(\sigma\operatorname{e x p}t X,X). $$ 

In particular, $V$ is complete; hence $V_{1}$ is defined and smooth on all of $G \times g$. Now let $\pi: G \times g$ be the projection onto $G$. Then

 $$ \operatorname{e x p}X=\pi\circ V_{1}(e,X). $$ 

Thus we have exhibited \exp as the composition of  $ C^{\infty} $ mappings, so  $ \exp $ is  $ C^{\infty} $. That  $ d\exp: g_0 \to G_e $ is the identity map is immediate, for  $ tX $ is a curve in g whose tangent vector at  $ t = 0 $ is X, and by part (a),  $ \exp tX $ is a curve in G whose tangent vector at  $ t = 0 $ is  $ X(e) $.

3.32 Theorem Let $\varphi: H \to G$ be a homomorphism, Then the following diagram is commutative:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//008e99d6-8a1d-4188-b841-b6c361e3463a/markdown_3/imgs/img_in_image_box_336_383_573_524.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A30Z%2F-1%2F%2F33b84f688ea60c087ba206f65cfcd86ae40397c67a23afdbecc891ec6c4a4377" alt="Image" width="24%" /></div>

PROOF Let $X\in\mathfrak{h}$. Then $t\mapsto\varphi(\exp tX)$ is a smooth curve in $G$ whose tangent at $0$ is $d\varphi(X(e))$. This is also a 1-parameter subgroup of $G$ since $\varphi$ is a homomorphism. But $t\mapsto\exp t(d\varphi(X))$ is the unique 1-parameter subgroup of $G$ whose tangent at $0$ is $(d\varphi(X))(e)$. Thus

 $$ \varphi(\exp t X)=\exp t\big(d\varphi(X)\big), $$ 

whence

 $$ \varphi(\exp X)=\exp\bigl(d\varphi(X)\bigr). $$ 

3.33 Proposition Let $(H,\varphi)$ be a Lie subgroup of $G$, and let $X\in\mathfrak{g}$. If $X\in d\varphi(\mathfrak{h})$, then $\exp tX\in\varphi(H)$ for all $t$. Conversely, if $\exp tX\in\varphi(H)$ for $t$ in some open interval, then $X\in d\varphi(\mathfrak{h})$.

PROOF If $X\in d\varphi(h)$, then $\exp tX\in\varphi(H)$ for all $t$, according to 3.32. On the other hand, if $\exp tX\in\varphi(H)$ for $t$ in some interval $I$, then for $t\in I$, the map $t\mapsto\exp tX$ can be expressed as a composition $\varphi\circ\alpha$ where $\alpha$, according to 1.62, is a smooth map of $I$ into $H$. Let $t_0\in I$, and let $\tilde{X}$ be the left invariant vector field on $H$ determined by $\dot{\alpha}(t_0)$. Then $d\varphi(\tilde{X})=X$.

3.34 Theorem Let A be an abstract subgroup of a Lie group G, and let a be a subspace of g. Let U be a neighborhood of 0 in g diffeomorphic under the exponential map with a neighborhood V of the identity in G. Suppose that

 $$ \operatorname{e x p}(U\cap a)=A\cap V. $$ 

Then A with the relative topology is a Lie subgroup of G, α is a subalgebra of g, and α is the Lie algebra of A.

PROOF We need only show that in the relative topology, the subgroup $A$ has a differentiable structure such that $(A,i)$ is a submanifold of $G$, where $i$ is the inclusion map. For then, according to 3.20, with this manifold structure (and no other) $A$ is a Lie subgroup of $G$, and it follows from 3.33 that the Lie algebra of $A$ is $a$. Let

 $$ \varphi=\exp\mid U\cap a\colon U\cap a\ \to\ \mathcal{A}\cap V. $$ 

Then the desired differentiable structure on $A$ is the maximal collection of smoothly overlapping coordinate systems containing the collection

 $$ \{(A\cap\sigma V,\varphi^{-1}\circ l_{\sigma^{-1}})\colon\sigma\in A\}. $$ 

### 3.35 Example We shall see that the exponential map

 $$ \mathtt{e x p}\colon\mathrm{g l}(n,\mathbb{C})\;\to\;\mathrm{G l}(n,\mathbb{C}) $$ 

for the complex general linear group is given by exponentiation of matrices. We shall now let $I$ rather than $e$ denote the identity matrix in $Gl(n,\mathbb{C})$. Let

 $$ e^{A}=I+A+\frac{A^{2}}{2!}+\cdots+\frac{A^{j}}{j!}+\cdots $$ 

for $A \in \mathrm{gl}(n, \mathbb{C})$. To see that this makes sense, that is, to see that the right-hand side of (2) converges, observe that in fact the right-hand side of (2) converges uniformly for $A$ in a bounded region of $\mathrm{gl}(n, \mathbb{C})$. For given a bounded region $\Omega$ of $\mathrm{gl}(n, \mathbb{C})$, there is a $\mu > 0$ such that for any matrix $A$ in this region, $|x_{ik}(A)| \leq \mu$ for each component $x_{ik}(A)$ of the matrix $A$. It follows easily by induction that $|x_{ik}(A^f)| \leq n^{(f-1)}\mu^f$. Thus, by the Weierstrass $M$-test, each of the series

 $$ \sum_{j=0}^{\infty}\frac{x_{ik}(A^{j})}{j!}\qquad(1\leq i\leq n;1\leq k\leq n) $$ 

converges uniformly for $A$ in $\Omega$. Thus the right-hand side of (2) converges uniformly for $A$ in $\Omega$.

Now let $S_{i}(A)$ be the $j$th partial sum of the series (2), that is,

 $$ S_{j}(A)=I+A+\frac{A^{2}}{2!}+\cdots+\frac{A^{j}}{j!}, $$ 

and let $B \in \mathrm{gl}(n,\mathbb{C})$. Then since $C \mapsto BC$ is a continuous map of $\mathrm{gl}(n,\mathbb{C})$ into itself, it follows that

 $$ B\left(\operatorname*{l i m}_{j\to\infty}S_{j}(A)\right)=\operatorname*{l i m}_{j\to\infty}\bigl(B S_{j}(A)\bigr). $$ 

In particular, if $B \in G l(n, \mathbb{C})$, then $B\left(\lim_{j \to \infty} S_j(A)\right)B^{-1} = \lim_{j \to \infty} BS_j(A)B^{-1}$, from which it follows that

 $$ B e^{A}B^{-1}=e^{B\Delta B^{-1}}. $$ 

There exists a $B\in G/(n,\mathbb{C})$ such that $BAB^{-1}$ is super-triangular; that is, all entries below the diagonal are zero. (Simply take $B$ to be the inverse of the matrix whose columns $v_1,\ldots,v_n$ are determined as follows: Let $I$ be the linear transformation of $\mathbb{C}^n$ whose matrix with respect to the canonical basis is $A$, let $v_1$ be an eigenvector of $I$, and inductively let $v_{i+1}$ be an eigenvector of $\pi_i\circ I\mid W_i$ where $W_i$ is any complement of the subspace $V_i$ of $C^n$ spanned by $v_1,\ldots,v_i$ and where $\pi_i$ is projection of $\mathbb{C}^n=V_i\oplus W_i$ onto $W_i$. If the diagonal entries of $BAB^{-1}$ are $\lambda_1,\ldots,\lambda_n$, then $e^{BAB^{-1}}$ is also super-triangular, with diagonal entries $e^{\lambda_1},\ldots,e^{\lambda_n}$. In particular, det $e^{BAB^{-1}}\neq0$, so it follows from (6) that

 $$ e^{A}\in\mathbb{G l}(n,\mathbb{C})\quad\mathrm{f o r~e a c h}\quad A\in\mathrm{g l}(n,\mathbb{C}). $$ 

Since the trace of a matrix is the sum of its eigenvalues, and the determinant is the product of its eigenvalues, we have also shown that

 $$ \det e^{A}=e^{\mathrm{t r a c e}A}. $$ 

Next we shall prove that

 $$ e^{A+B}=e^{A}e^{B}\quad\mathrm{i f}\quad A B=B A. $$ 

By definition,  $ e^{A+B} = \lim_{j \to \infty} S_j(A + B) $. It follows from the fact that matrix multiplication gives a continuous map of  $ \mathrm{gl}(n, \mathbb{C}) \times \mathrm{gl}(n, \mathbb{C}) $ into  $ \mathrm{gl}(n, \mathbb{C}) $ that  $ e^A e^B = \lim_{j \to \infty} S_j(A) \cdot S_j(B) $. So to prove (9), it suffices to show that

 $$ \operatorname*{l i m}_{j\to\infty}\left\{S_{j}(A)S_{j}(B)-S_{j}(A+B)\right\}=0. $$ 

Now,

 $$ S_{j}(A)S_{j}(B)-S_{j}(A+B)=\sum\frac{B^{l}A^{k}}{l!k!} $$ 

where the sum is over all integers $l$ and $k$ for which $1 \leq l \leq j$, $1 \leq k \leq j$, and $j + 1 \leq l + k \leq 2j$. If $\mu > 1$ is an upper bound for the absolute value of each of the entries of $A$ and $B$, then it follows that each entry of the right-hand side of (11) is bounded in absolute value by

 $$ \begin{array}{r}{\sum\frac{n^{(i+k-1)}\mu^{(i+k)}}{|I!k!}\leq\frac{(n\mu)^{8j}(j^{8})}{[j/2]!}}\end{array} $$ 

where [j/2] is the greatest integer less than or equal to j/2. The estimate on the right-hand side of (12) goes to zero as $j \to \infty$, which proves (10) and hence proves (9).

Consider the map $t \mapsto e^{t\Delta}$ of $\mathbb{R}$ into $Gl(n,\mathbb{C})$. It is smooth since the real and imaginary components of each entry of $e^{t\Delta}$ are power series in $t$ with infinite radii of convergence. Its tangent vector at $0$ is $A$ (simply differentiate the power series term by term), and this map is a homomorphism by (9).

Thus $t \mapsto e^{t\mathcal{A}}$ is the unique 1-parameter subgroup of $Gl(n,\mathbb{C})$ whose tangent vector at 0 is $A$. So the exponential map (1) for $Gl(n,\mathbb{C})$ is given by exponentiation of matrices:

 $$ \operatorname{e x p}(A)=e^{A}\qquad\big(A\in\operatorname{g l}(n,\mathbb{C})\big). $$ 

If $A \in \mathrm{gl}(n, \mathbb{R})$, then $e^A \in \mathrm{Gl}(n, \mathbb{R})$, and $A \to e^A$ is the exponential map for the real general linear group. Similarly, the exponential map

 $$ \operatorname{e x p}\colon\operatorname{E n d}(V)\;\to\;\operatorname{A u t}(V), $$ 

where $V$ is a real or complex vector space, is given by exponentiation of endomorphisms. If $l \in \mathrm{End}(V)$, then

 $$ \exp(l)=e^{l}=1+l+\frac{l^{2}}{2!}+\cdots+\frac{l^{s}}{j!}+\cdots $$ 

where $l^{\prime\prime}$ means “$l$ composed with itself $j$ times,” and where $l$ is the identity transformation.

3.36 Remarks If $\varphi: G \to \mathrm{Aut}(V)$ is a representation, and $X \in \mathfrak{g}$, then it follows from 3.35(15) and 3.32 that

 $$ \varphi(\exp X)=1+d\varphi(X)+\frac{\left(d\varphi(X)\right)^{8}}{2!}+\cdots, $$ 

and it follows from 3.32 and 3.9(2) that

 $$ d\varphi(X)=\lim_{t\to0}\frac{\varphi(\exp tX)-1}{t}=\left.\frac{d}{dt}\right|_{t=0}(\varphi(\exp tX)). $$ 

3.37 Subgroups of $GI(n,\mathbb{C})$ Using 3.34 and 3.35, we shall now obtain some of the classical Lie subgroups of $GI(n,\mathbb{C})$ by exponentiating subalgebras of $\mathfrak{gl}(n,\mathbb{C})$. We already have one example, namely, $GI(n,\mathbb{R})$ is a closed Lie subgroup of $GI(n,\mathbb{C})$ with Lie algebra $\mathfrak{gl}(n,\mathbb{R}) \subset \mathfrak{gl}(n,\mathbb{C})$. Let $A \in \mathfrak{gl}(n,\mathbb{C})$. Then the transpose of $A$ is the matrix $A^t$ such that $(A^t)_{ij} = A_{ji}$; and the complex conjugate of $A$ is the matrix $\bar{A}$ whose $ij$th entry $(\bar{A})_{ij}$ is the complex conjugate $\overline{A_{ij}}$ of $A_{ij}$. And $n$, of course, is an integer $\geq 1$.

(a) Unitary group

 $$ U(n)=\{A\in G l(n,\mathbb{C})\colon A^{-1}=\overline{{A^{t}}}\}. $$ 

(b) Special linear group

 $$ S l(n,\mathbb{C})=\{A\in G l(n,\mathbb{C})\colon\operatorname*{d e t}A=1\}. $$ 

(c) Complex orthogonal group

 $$ O(n,\mathbb{C})=\{A\in G l(n,\mathbb{C})\colon A^{-1}=A^{\mathfrak{t}}\}. $$ 

Each of these is an abstract subgroup and a closed subset of $GI(n,\mathbb{C})$. We shall use 3.34 to show that they are Lie subgroups. Their Lie algebras will be

(a') Skew-hermitian matrices

 $$ \mathbf{u}(n)=\{A\in\mathfrak{g l}(n,\mathbb{C})\colon\bar{A}+\mathcal{A}^{t}=0\}. $$ 

(b') Matrices of trace 0

 $$ \mathtt{s l}(n,\mathbb{C})=\{A\in\mathsf{g l}(n,\mathbb{C})\colon\mathrm{t r a c e}A=0\}. $$ 

(c') Skew-symmetric matrices

 $$ \mathfrak{d}(n,\mathbb{C})=\{A\in\mathfrak{g l}(n,\mathbb{C})\colon A+A^{t}=0\}. $$ 

Each of these examples is a subalgebra of $\mathrm{gl}(n,\mathbb{C})$. To apply 3.34, let $U$ be a neighborhood of $0$ in $\mathrm{gl}(n,\mathbb{C})$, diffeomorphic under the exponential map with a neighborhood $V$ of the identity in $Gl(n,\mathbb{C})$. We can assume, in addition, that if $A\in U$, then $\widetilde{A}, A^t$, and $-A$ belong to $U$, and $|\mathrm{trace}A|<2\pi$. For let $W$ be a neighborhood of $0$ in $\mathrm{gl}(n,\mathbb{C})$ that is small enough for the exponential map to be a diffeomorphism and also small enough for the trace condition to be satisfied, and then let $U=W\cap\overline{W}\cap W^t\cap(-W)$. We shall also assume that $\exp(U\cap\mathrm{gl}(n,\mathbb{R}))=Gl(n,\mathbb{R})\cap V$.

If $A \in U \cap u(n)$, then $(\overline{e^A})^t = e^{\overline{A}^t} = e^{-\overline{A}};$ hence $(\overline{e^A})^t e^A = e^{-\overline{A}} e^A = e^B = I$, which implies that $e^A \in U(n) \cap V$. Conversely, suppose that $A \in U$ and that $e^A \in U(n) \cap V$. Then $e^{-A} = (e^A)^{-1} = (\overline{e^A})^t = e^{\overline{A}^t}$, which implies that $-A = \overline{A}^t$ since $-A$ and $\overline{A}^t$ also belong to $U$ and since the exponential map is 1:1 on $U$. Thus $A \in U \cap u(n)$. It follows from 3.34 that $U(n)$ is a closed Lie subgroup of $Gl(n, \mathbb{C})$ with Lie algebra $u(n)$. A similar argument shows that $O(n, \mathbb{C})$ is a closed Lie subgroup of $Gl(n, \mathbb{C})$ with Lie algebra $o(n, \mathbb{C})$.

If $A \in \mathrm{sl}(n,\mathbb{C})$, then by 3.35(8), $\det e^A = 1$; hence $e^A \in \mathrm{Sl}(n,\mathbb{C})$. Conversely, if $\det e^A = 1$, then according to 3.35(8), $\mathrm{trace} A = (2\pi i)j$ for some integer $j$. If in addition $A \in U$, then $\mathrm{trace} A = 0$. Thus 3.34 implies that $\mathrm{Sl}(n,\mathbb{C})$ is a closed Lie subgroup of $\mathrm{Gl}(n,\mathbb{C})$ with Lie algebra $\mathrm{sl}(n,\mathbb{C})$.

It follows immediately from 3.34 and from considerations as given above that the special unitary group $SU(n)$, which is by definition $U(n)\cap S(n,\mathbb{C})$, is a closed Lie subgroup of $G(n,\mathbb{C})$ with Lie algebra $\mathfrak{s}(n)$ the subalgebra of $\mathfrak{g}(n,\mathbb{C})$ consisting of skew-hermitian matrices of trace $0$; the real special linear group $S(n,\mathbb{R})$, which is by definition $S(n,\mathbb{C})\cap G(n,\mathbb{R})$, is a closed Lie subgroup of $G(n,\mathbb{R})$ with Lie algebra $\mathfrak{s}(n,\mathbb{R})$ the real matrices of trace $0$; the orthogonal group $O(n)$, which is by definition $\mathcal{G}(n)\cap G(n,\mathbb{R})$, is a closed Lie subgroup of $G(n,\mathbb{R})$ with Lie algebra $o(n)$ the real skew-symmetric matrices; and the special orthogonal group $SO(n)$, which is by definition $O(n)\cap S(n,\mathbb{R})$, is a closed Lie subgroup of $G(n,\mathbb{R})$ also with Lie algebra $o(n)$ the real skew-symmetric matrices.

Each of these examples is a closed subgroup of either $GI(n,\mathbb{R})$ or $GI(n,\mathbb{C})$, and it follows from either 3.34 or 3.21 that in each case the Lie topology is the relative topology.

The unitary group is compact since not only is it closed, but also it is bounded in $GI(n,\mathbb{C})$, for $A^t\bar{A}=I$ implies that $\sum_j|A_{ij}|^a=1$ for each $i$, which implies that $|A_{ij}|^a\leq1$. It follows that $SU(n)$, $O(n)$, and $SO(n)$ are also compact.

The dimensions of these Lie groups are easily computed from their Lie algebras. $U(n)$ has dimension $n^2$; $Sl(n,\mathbb{C})$ has dimension $2n^2 - 2$; $O(n,\mathbb{C})$ has dimension $n(n - 1)$; $SU(n)$ has dimension $n^2 - 1$; $Sl(n,\mathbb{R})$ has dimension $n^2 - 1$; $O(n)$ and $SO(n)$ both have dimension $n(n - 1)/2$.

##### CONTINUOUS HOMOMORPHISMS

3.38 Theorem Let $\varphi: \mathbb{R} \to G$ be a continuous homomorphism of the real line $\mathbb{R}$ into the Lie group $G$. Then $\varphi$ is $C^\infty$.

PROOF It suffices to prove that $\varphi$ is $C^{\infty}$ on a neighborhood of $0$, for then it follows from composition with suitable left translations that $\varphi$ is $C^{\infty}$ everywhere. Let $V$ be a neighborhood of $e\in G$ diffeomorphic with a neighborhood $U$ of $0\in g$ under the exponential map. We can assume that $U$ is starlike, that is, $tX\in U$ for $0\leq t\leq 1$ whenever $X\in U$, and we let

 $$ U^{\prime}=\{X/2\colon X\in U\}. $$ 

Choose $t_0 > 0$ small enough so that $\varphi(t) \in \exp(U')$ for $|t| \leq t_0$. Let $n$ be a positive integer. Then there are uniquely determined elements $X$ and $Y$ of $U'$ such that $\exp X = \varphi(t_0/n)$ and $\exp Y = \varphi(t_0)$. We claim that $nX = Y$. Since

 $$ \operatorname{e x p}(n X)=\varphi(t_{0})=\operatorname{e x p}(Y), $$ 

and since  $ \exp $ is injective on  $ U' $, we need only show that  $ nX \in U' $. Now,  $ X \in U' $, so let  $ 1 \leq j < n $, and assume that  $ jX \in U' $. We will prove that  $ (j+1)X \in U' $. Now,  $ (j+1)X \in U $, and  $ \exp((j+1)X) = \varphi((j+1)t_0/n) $ which by assumption belongs to  $ \exp(U') $. Since  $ \exp $ is injective on  $ U $, it follows that  $ (j+1)X \in U' $. Hence  $ nX \in U' $ and  $ nX = Y $, as claimed. Now, let  $ n_1 $ be an integer with  $ 0 < |m| \leq n $. If  $ m $ is positive, then  $ \varphi(m t_0/n) = \varphi(t_0/n)^m = \exp(Y/n)^m = \exp(m Y/n) $. If  $ m $ is negative, then also  $ \varphi(m t_0/n) = \varphi((-m)t_0/n)^{-1} = \exp((-m)Y/n)^{-1} = \exp(m Y/n) $. It follows by continuity that  $ \varphi(t) = \exp(t/Y/t_0) $ for  $ |t| \leq t_0 $. Thus  $ \varphi $ is  $ C^\infty $.

3.39 Theorem Let $\varphi: H \to G$ be a continuous homomorphism of Lie groups. Then $\varphi$ is $C^\infty$.

PROOF Let $H$ be of dimension $d$, and let $X_{1}, \ldots, X_{d}$ be a basis of $b$. The map $\alpha: \mathbb{R}^{d} \to H$ defined by

(1)

 $$ \alpha(t_{1},\ldots,t_{d})=(\exp t_{1}X_{1})\cdots(\exp t_{d}X_{d}) $$ 

is $C^{\infty}$, and is non-singular at $0\in\mathbb{R}^{d}$ by 3.31(d); so there is a neighborhood $V$ of $0\in\mathbb{R}^{d}$ diffeomorphic under $\alpha$ with a neighborhood $U$ of $e$ in $H$. Now, $t\mapsto\varphi(\exp tX_{t})$ is a continuous homomorphism of $\mathbb{R}$ into $G$, and so is $C^{\infty}$ by 3.38. Thus $\varphi\circ\alpha$ is $C^{\infty}$, and therefore $\varphi\mid U$, which can be expressed as $(\varphi\circ\alpha)\circ\alpha^{-1}\mid U$, is $C^{\infty}$. Since $\varphi\mid\sigma U=\mid\varphi(\sigma)\circ\varphi\circ\sigma\mid\sigma U$, $\varphi$ is $C^{\infty}$ on all of $H$.

3.40 Definition A topological group $G$ is an abstract group $G$ which has a topology such that the map $(\sigma,\tau) \mapsto \sigma\tau^{-1}$ of $G \times G \to G$ is continuous.

3.41 Corollary to Theorem 3.39 A second countable locally Euclidean topological group can have at most one differentiable structure making it into a Lie group.

PROOF The identity map would give a diffeomorphism of any two such differentiable structures.

One of the outstanding problems in the theory of Lie groups was that of deciding whether every connected locally Euclidean topological group has a differentiable structure which makes it into a Lie group. The problem was posed by Hilbert in his famous address to the International Congress of Mathematics in 1900, and was solved with an affirmative answer by Gleason together with Montgomery and Zippen in 1952; see [20].

We have dealt exclusively with the $C^{\infty}$ structure on Lie groups. It can be shown [23] that the $C^{\infty}$ structure on a Lie group contains an analytic structure, that is, a collection of coordinate systems which overlap analytically (the compositions $\varphi_{\alpha}\circ\varphi_{\beta}^{-1}$ of coordinate maps being locally represented by convergent power series). In this context, the analog of 3.39 would state that every continuous homomorphism of Lie groups is analytic, from which it follows that the $C^{\infty}$ structure on a Lie group contains a unique analytic structure.

##### CLOSED SUBGROUPS

3.42 Theorem Let G be a Lie group, and let A be a closed abstract subgroup of G. Then A has a unique manifold structure which makes A into a Lie subgroup of G.

According to 3.21, the topology in this manifold structure on A must be the relative topology.

PROOF Uniqueness has been proved in 3.20. Let

 $$ a=\{X\in\mathfrak{g}\colon\operatorname{e x p}{t X\in A}\mathrm{~f o r~a l l~}t\in\mathbb{R}\}. $$ 

The idea of the proof is to show that $a$ is a subspace of $g$, and to apply 3.34. It is clear from the definition (1) that if $X \in a$, then also $tX \in a$ for any $t \in \mathbb{R}$. Now, let $X, Y \in a$. Suppose that

 $$ \operatorname*{l i m}_{n\to\infty}\Big(\mathtt{e x p}\frac{t}{n}X\mathtt{e x p}\frac{t}{n}Y\Big)^{n}=\mathtt{e x p}\big(t(X+Y)\big). $$ 

Since $A$ is closed, the left-hand side of (2) belongs to $A$. Thus (2) implies that $(X + Y) \in a$. Assuming (2) for the moment, we have proved that $a$ is a subspace of $g$ and shall use this to complete the proof of the theorem. We shall return to the proof of (2) in a separate lemma.

The theorem will follow from 3.34 once we have shown that there exists a neighborhood U of 0 in g, diffeomorphic under the exponential map with a neighborhood V of e in G such that

 $$ \operatorname{e x p}(U\cap a)=V\cap A. $$ 

Suppose, on the contrary, that no such $U$ exists. Then there is a neighborhood $W$ of 0 in $a$ and a sequence $\{\sigma_k\} \subset A$ such that $\sigma_k \to e$ in $G$ and

 $$ \sigma_{k}\notin\operatorname{e x p}(W). $$ 

Let $b$ be any complementary subspace to $a$ in $g$. It follows from 3.31(d) that the map $\alpha: a \times b \to G$ defined by $\alpha(X, Y) = \exp X \exp Y$ is $C^\infty$ and non-singular at $(0,0)$. Thus there are neighborhoods $W_a \subset W$ of $0$ in $a$ and $W_b$ of $0$ in $b$ such that $\alpha \big| W_a \times W_b$ is a diffeomorphism of $W_a \times W_b$ with a neighborhood $\tilde{V}$ of $e$ in $G$. If we can choose $W_b$ small enough that

 $$ A\cap\operatorname{e x p}(W_{\flat}-\{0\})=\varnothing, $$ 

then we can reach a contradiction as follows. For $k$ large enough, $\sigma_k \in \tilde{V}$, and thus $\sigma_k = \exp X_k \exp Y_k$ for $X_k \in W_a$ and $Y_k \in W_b$, where $Y_k \neq 0$ by (4). But $\sigma_k \in A$, as also $\exp X_k \in A$; so $\exp Y_k \in A$, contradicting (5).

Finally, we show that $W_b$ can be chosen satisfying (5). Again we argue by contradiction. Suppose that there is a sequence $\{Y_i\} \subset W_b$ such that $Y_i \neq 0$, $Y_i \to 0$, and $\exp Y_i \in A$. Then there is a subsequence $\{Y_j\}$ and a sequence $\{t_j\}$ of positive real numbers with $t_j \to 0$ such that the sequence $\{Y_j/t_j\}$ converges to some $Y \neq 0$ in $W_b$ (choose a norm on the vector space $W_b$, and let $t_i$ be the norm of $Y_i$). For $t > 0$, let $n_j(t)$ be the largest integer less than or equal to $(t/t_j)$. Then

 $$ \begin{array}{r}{\frac{t}{t_{j}}-1<n_{j}(t)\leq\frac{t}{t_{j}},}\end{array} $$ 

so  $ \lim_{t \to \infty} t_j n_j(t) = t $. Thus

 $$ \mathbf{e x p}\;t Y=\mathbf{e x p}\biggl(\operatorname*{l i m}_{j\to\infty}n_{j}(t)Y_{j}\biggr)=\operatorname*{l i m}_{j\to\infty}(\mathbf{e x p}\;Y_{j})^{n_{j}(t)}, $$ 

which belongs to $A$. Since $\exp(-tY) = (\exp{tY})^{-1}$, then $\exp{tY} \in A$ for all real numbers $t$, which implies that $Y \in a$. This contradicts the fact that $Y$ is a non-zero element of $W_b$.

To complete the proof we need the following lemma, which clearly implies (2).

Lemma Let G be a Lie group with Lie algebra g. If $X, Y \in \mathfrak{g}$, then for $t$ sufficiently small,

 $$ \operatorname{e x p}t X\operatorname{e x p}t Y=\operatorname{e x p}\{t(X+Y)+O(t^{s})\}, $$ 

where $O(t^{8})$ denotes a g-valued $C^{\infty}$ function of $t$ such that $(1/t^{8})O(t^{8})$ is bounded at $t=0$.

PROOF For $t$ small enough, there is a $C^{\infty}$ curve $Z(t)$ in $g$ such that

 $$ \operatorname{e x p}t X\operatorname{e x p}t Y=\operatorname{e x p}Z(t). $$ 

Since the tangent vector to the curve

 $$ t\mapsto\exp t X\exp t Y $$ 

at $t=0$ is $X(e)+Y(e)$ (see Exercise 11), it follows that the tangent vector to $Z(t)$ at $t=0$ is $X+Y$, so the Taylor expansion with integral remainder of $Z(t)$ about $t=0$ has the form

 $$ Z(t)=t(X+Y)+O(t^{s}), $$ 

where $O(t^{2})$ is a $C^{\infty}$ g-valued function of $t$ such that $(1/t^{2})O(t^{2})$ is bounded at $t=0$. From (7) and (8) we obtain (6).

3.43 Theorem Let $\psi: G \to K$ be a homomorphism of Lie groups. If $A = \ker \psi$ and $a = \ker d\psi$, then $A$ is a closed Lie subgroup of $G$ with Lie algebra a.

PROOF $A$ is a closed abstract subgroup of $G$, hence, by 3.42, is a Lie subgroup of $G$. If $X \in g$, then according to 3.33 (with $H = A$ and $\varphi$ the inclusion map), $X$ belongs to the Lie algebra of $A$ if and only if $\exp t X \in A$ for all $t \in \mathbb{R}$, and this occurs if and only if $\psi(\exp t X) = e$ for all $t \in \mathbb{R}$. By 3.32, this latter condition is equivalent to having $\exp t \, d\psi(X) = e$ for all $t \in \mathbb{R}$, and this occurs if and only if $d\psi(X) = 0$ or $X \in a$.

##### THE ADJOINT REPRESENTATION

3.44 Definitions Let $M$ be a manifold, and let $G$ be a Lie group. $A$ $C^{\infty}$ map $\mu: G \times M \to M$ such that

 $$ \mu(\sigma\tau,m)=\mu\big(\sigma,\mu(\tau,m)\big),\qquad\mu(e,m)=m $$ 

for all $\sigma, \tau \in G$ and $m \in M$ is called an action of $G$ on $M$ on the left. If $\mu: G \times M \to M$ is an action of $G$ on $M$ on the left, then for a fixed $\sigma \in G$ the map $m \mapsto \mu(\sigma, m)$ is a diffeomorphism of $M$ which we shall denote by $\mu_{\sigma}$. Similarly, a $C^{\infty}$ map $\mu: M \times G \to M$ such that

 $$ \mu(m,\sigma\tau)=\mu\big(\mu(m,\sigma),\tau\big),\qquad\mu(m,e)=m $$ 

for all $\sigma, \tau \in G$ and $m \in M$ is called an action of $G$ on $M$ on the right.

3.45 Theorem Let $\mu: G \times M \to M$ be an action of $G$ on $M$ on the left. Assume that $m_0 \in M$ is a fixed point, that is, $\mu_\sigma(m_0) = m_0$ for each $\sigma \in G$. Then the map

 $$ \psi\colon G\to\mathrm{A u t}(M_{m_{0}}) $$ 

defined by

 $$ \psi(\sigma)=d\mu_{o}\mid M_{m_{o}} $$ 

is a representation of G.

PROOF  $ \psi $ is a homomorphism for

 $$ \psi(\sigma\tau)=d\mu_{\sigma\tau}\left|M_{m_{0}}=d(\mu_{\sigma}\circ\mu_{\tau})\right|M_{m_{0}}=\psi(\sigma)\circ\psi(\tau). $$ 

It remains only to prove that $\psi$ is $C^{\infty}$. For this, it suffices to prove that $\psi$ composed with an arbitrary coordinate function on $\mathrm{Aut}(M_{m_0})$ is $C^{\infty}$. Now, one gets a coordinate system on $\mathrm{Aut}(M_{m_0})$ by choosing a basis for $M_{m_0}$ and then by using this basis to identify $\mathrm{Aut}(M_{m_0})$ with non-singular matrices. One gets the matrix associated with an element of $\mathrm{Aut}(M_{m_0})$ by applying this element to the basis of $M_{m_0}$ and then applying the dual basis. So it suffices to prove that if $v_0 \in M_{m_0}$ and if $\alpha \in M_{m_0}^*$, then

 $$ \sigma\mapsto\alpha\left(d\mu_{\sigma}(v_{0})\right) $$ 

is a $C^{\infty}$ function on $G$. For (3), it suffices to prove that

 $$ \sigma\mapsto d\mu_{\sigma}(v_{0}) $$ 

is a $C^{\infty}$ map of $G$ into $M_{m_{0}}$, or equivalently that (4) is a $C^{\infty}$ map of $G$ into $T(M)$. But (4) is exactly the composition of $C^{\infty}$ maps

 $$ G\to T(G)\times T(M)\to T(G\times M)\to T(M) $$ 

in which the first map sends $\sigma \mapsto \big((\sigma,0),(m_0,v_0)\big)$, the second map is the canonical diffeomorphism of $T(G) \times T(M)$ with $T(G \times M)$, and the third map is $d\mu$. Thus $\psi$ is $C^\infty$.

3.46 The Adjoint Representation A Lie group G acts on itself on the left by inner automorphisms:

 $$ a\colon G\times G\to G,\qquad a(\sigma,\tau)=\sigma\tau\sigma^{-1}=a_{\sigma}(\tau). $$ 

The identity is a fixed point of this action. Hence, by 3.45, the map

 $$ \sigma\mapsto d a_{\sigma}\mid G_{e}\cong g $$ 

is a representation of $G$ into $\operatorname{Aut}(g)$. This is called the adjoint representation and is denoted by

 $$ \mathsf{A d}\colon G\to\mathsf{A u t}(\mathfrak{g}). $$ 

We let the differential of the adjoint representation be denoted by ad.

 $$ d(\mathbf{A d})={\cdot}\mathbf{a d}, $$ 

and we denote $\mathrm{Ad}(\sigma)$ by $\mathrm{Ad}_{\sigma}$ and $\mathrm{ad}(X)$ by $\mathrm{ad}_{X}$. Thus by 3.32 we have a commutative diagram

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//e006bf97-c486-454f-b40d-7a66ef2d28b8/markdown_1/imgs/img_in_image_box_329_219_602_347.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2F138d535ac3aab9115d34c44305ad9635921517883bdc4555f65bc4b94b31989a" alt="Image" width="27%" /></div>

Also applying 3.32 to the automorphism $a_{\sigma}$ of $G$, we obtain the commutative diagram

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//e006bf97-c486-454f-b40d-7a66ef2d28b8/markdown_1/imgs/img_in_image_box_340_404_587_530.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2Fb961bab64d8cfc67287c764901315bb5444af0b9fe2aaa20bb6dfdec8f990060" alt="Image" width="25%" /></div>

In other words,

 $$ \operatorname{e x p}t\operatorname{A d}_{\sigma}(X)=\sigma(\operatorname{e x p}t X)\sigma^{-1}. $$ 

In the special case in which $G = \mathrm{Aut}(V)$, the above diagrams become

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//e006bf97-c486-454f-b40d-7a66ef2d28b8/markdown_1/imgs/img_in_image_box_297_635_642_767.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2Ffa5860e4fca410b7d16d653f4ce67331744850752006c43531425be5ad7aced7" alt="Image" width="35%" /></div>

<div style="text-align: center;"><div style="text-align: center;">(8)</div> </div>

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//e006bf97-c486-454f-b40d-7a66ef2d28b8/markdown_1/imgs/img_in_image_box_299_797_601_924.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2Fc66a14850408cfdabc145de8b8bf7d511a0df3d3bdd98e744d6f1a08c07028b2" alt="Image" width="30%" /></div>

where  $ B \in \text{Aut}(V) $. If in addition  $ C \in \text{End}(V) $, then

 $$ \mathsf{A d}_{B}(C)=B\circ C\circ B^{-1}. $$ 

For from 3.36(2), using 3.35(15) and 3.35(6), we obtain

 $$ \begin{align*}\mathrm{Ad}_{B}(C)&=\frac{d}{dt}\bigg|_{t=0}\big(a_{B}(\exp t C)\big)=\frac{d}{dt}\bigg|_{t=0}(B\circ e^{tC}\circ B^{-1})\\&=\frac{d}{dt}\bigg|_{t=0}e^{t B\circ C\circ B^{-1}}=B\circ C\circ B^{-1}.\end{align*} $$ 

Similarly, in the case in which $G = Gl(n, \mathbb{R})(\text{or } Gl(n, \mathbb{C}))$ and $B \in Gl(n, \mathbb{R})$ and $C \in gl(n, \mathbb{R})$, then

 $$ \mathrm{A d}_{B}(C)=B C B^{-1}. $$ 

3.47 Proposition Let G be a Lie group with Lie algebra g, and let X, Y ∈ g. Then

(1)

 $$ \mathbf{a d}_{X}Y=[X,Y]. $$ 

PROOF By 3.36(2),

(2)

 $$ \begin{align*}\mathrm{ad}_{X}Y&=\left(\frac{d}{dt}\bigg|_{t=0}\mathrm{Ad}(\exp tX)\right)Y\\&=\frac{d}{dt}\bigg|_{t=0}\mathrm{Ad}_{\exp tX}(Y)=\frac{d}{dt}\bigg|_{t=0}d(a_{\exp tX})(Y).\end{align*} $$ 

Thus if $X_{t}$ denotes, as usual, the 1-parameter group of diffeomorphisms associated with $X$, then

 $$ \begin{aligned}{\operatorname{a d}_{\underline{{X}}}Y(e)}&{{}=\frac{d}{d t}\bigg|_{t=0}d(r_{\operatorname{e x p}(-t\underline{{X}})})\big(d(l_{\operatorname{e x p}t\underline{{X}}})(Y(e))\big)}\\ {}&{{}=\frac{d}{d t}\bigg|_{t=0}d(r_{\operatorname{e x p}(-t\underline{{X}})})(Y\big|_{\operatorname{e x p}t\underline{{X}}})}\\ {}&{{}=\frac{d}{d t}\bigg|_{t=0}d(X_{-t})(Y_{X_{t}(e)})}\\ {}&{{}=(L_{\underline{{X}}}Y)(e)=[X,Y](e).}\\ \end{aligned} $$ 

The last equality follows from 2.25(b). Since $\operatorname{ad}_{X}Y$ and $[X,Y]$ are both left invariant, (1) is an immediate consequence of (3).

3.48 Theorem Let $A \subseteq G$ be a connected Lie subgroup of a connected Lie group $G$. Then $A$ is a normal subgroup of $G$ if and only if the Lie algebra $a$ of $A$ is an ideal in $g$.

PROOF Assume that a is an ideal in g. Let  $ Y \in a $, let  $ X \in g $, and let  $ \sigma = \exp X $. Then

(1)

 $$ \begin{aligned}{{})\quad\sigma(\operatorname{e x p}Y)\sigma^{-1}}&{{}=\operatorname{e x p}\operatorname{A d}_{\sigma}(Y)}\\ {}&{{}=\operatorname{e x p}\bigl((\operatorname{e x p}\operatorname{a d}_{X})(Y)\bigr)}\\ \end{aligned} $$ 

 $$ \exp\left(Y+[X,Y]+\frac{(\mathrm{ad})^{2}X}{2!}(Y)+\cdots\right). $$ 

Under the assumption that a is an ideal in g, the series in the last term in (1) converges to an element of a, so that

 $$ \sigma(\exp Y)\sigma^{-1}\in A. $$ 

Now, by 3.18 and 3.31(d), $A$ is generated by elements of the form $\exp Y$, and $G$ is generated by elements of the form $\exp X$. This, together with (2), implies that $A$ is a normal subgroup of $G$.

Conversely, assume that $A$ is normal in $G$. Let $s$ and $t$ be real numbers, let $Y \in \alpha$ and $X \in g$, and let $\sigma = \exp t X$. Then, according to (1),

 $$ \sigma(\operatorname{e x p}s Y)\sigma^{-1}=\operatorname{e x p}\operatorname{A d}_{\sigma}(s Y)=\operatorname{e x p}s\big\{(\operatorname{e x p}\operatorname{a d}_{t X})(Y)\big\}. $$ 

Since $A$ is normal, $\sigma(\exp sY)\sigma^{-1}\in A$; so it follows from (3) and 3.33 that $(\exp ad_{tX})(Y)\in a$ for all $t\in\mathbb{R}$. Now

(4)

 $$ \begin{aligned}{(\operatorname{e x p}\operatorname{a d}_{t X})(Y)}&{{}=\big(\operatorname{e x p}t(\operatorname{a d}_{X})\big)(Y)}\\ {}&{{}=Y+t[X,Y]+\frac{t^{8}}{2!}\left[X,[X,Y]\right]+\cdots,}\\ \end{aligned} $$ 

which is a smooth curve in a whose tangent vector at $t = 0$ is $[X, Y]$. Thus $[X, Y] \in \alpha$, and $\alpha$ is an ideal in $g$.

### 3.49 Definitions

(a) Center of g = \{X ∈ g: [X, Y] = 0 for all Y ∈ g\}.

(b) Center of  $ G = \{\sigma \in G: \sigma \tau = \tau \sigma \text{ for all } \tau \in G\} $.

3.50 Theorem Let G be a connected Lie group. Then the center of G is the kernel of the adjoint representation.

PROOF Let  $ \sigma $ belong to the center of G, and let  $ X \in \mathfrak{g} $. Then

 $$ \operatorname{e x p}t X=\sigma(\operatorname{e x p}t X)\sigma^{-1}=\operatorname{e x p}t\operatorname{A d}_{\sigma}(X) $$ 

for all $t\in\mathbb{R}$. Thus $X=\mathrm{Ad}_{e}(X)$; so $\sigma\in\ker(\mathrm{Ad})$. Conversely, let $\sigma\in\ker(\mathrm{Ad})$. Then (1) again holds, so $\sigma$ commutes with every element in a neighborhood of $e$ in $G$. Since $G$ is connected, $\sigma$ commutes with every element of $G$. Thus $\sigma$ lies in the center of $G$.

Corollary (a) Let G be a connected Lie group. Then the center of G is a closed Lie subgroup of G with Lie algebra the center of g.

PROOF This corollary is an immediate consequence of 3.50 and 3.43.

Corollary (b) A connected Lie group G is abelian if and only if its Lie algebra g is abelian.

3.51 Proposition Let $X$, $Y$ belong to the Lie algebra $\mathfrak{g}$ of a Lie group $G$. Then

 $$ [X,Y]=0\;\Rightarrow\;\operatorname{e x p}(X+Y)=\operatorname{e x p}X\operatorname{e x p}Y. $$ 

PROOF The subspace a of g spanned by X and Y is a subalgebra of g, and the corresponding connected Lie subgroup A of G is abelian. Let

 $$ \alpha(t)=\exp t X\exp t Y. $$ 

Then $\alpha$ is a $C^{\infty}$ map of $\mathbb{R}$ into $G$ and is a homomorphism since $A$ is abelian. The tangent vector to $\alpha$ at $0$ is $X(e) + Y(e)$ (see Exercise 11), so that

 $$ \exp{t}X\exp{t}Y=\exp{t}(X+Y) $$ 

for all t.

3.52 Remark Recall that in 3.27 we stated Ado's theorem which asserts that any Lie algebra g has a faithful representation in some $\mathrm{gl}(n,\mathbb{R})$ from which it follows that there is a Lie group with Lie algebra g. If g has trivial center, we can get such a faithful representation from the adjoint representation. Simply define $ad:g \to \mathrm{Erd}(g)$ by $ad_x(Y) = [X, Y]$, and check that this is a Lie algebra homomorphism. If g has trivial center, ad is one-to-one; so we have a faithful representation of g in $\mathrm{End}(g)$. This together with 3.19 gives a simple proof that every Lie algebra with trivial center is the Lie algebra of some Lie group.

## AUTOMORPHISMS AND DERIVATIONS OF BILINEAR OPERATIONS AND FORMS

3.53 Definitions Let $V$ be a finite dimensional real or complex vector space. A bilinear operation on $V$ is a linear map $\psi: V\otimes V \to V$ where the tensor product is taken over the real (resp. complex) numbers when $V$ is a real (resp. complex) vector space. We shall use the notation

 $$ \psi(v\otimes w)=\{v,w\}. $$ 

(a) We let

 $$ A_{v}(V)=\{\alpha\in\mathbf{A u t}(V)\colon\alpha\{v,w\}=\{\alpha(v),\alpha(w)\}\mathrm{f o r~a l l}v,w\in V\}. $$ 

The elements of $A_{w}(V)$ are the automorphisms of $V$ which preserve the bilinear operation $\psi$.

(b) We let

 $$ \mathfrak{d}_{w}=\{I\in\mathbb{E n d}(V)\colon I\{v,w\}=\{I(v),w\}+\{v,l(w)\}\mathrm{~f o r~a l l~}v,w\in V\}. $$ 

Elements of  $ b_{\psi} $ are called derivations of the bilinear operation  $ \psi $.

3.54 Theorem $A_{v}(V)$ is a closed Lie subgroup of $\mathrm{Aut}(V)$ with Lie algebra $\partial_{v}$.

PROOF It is easy to check that $b_{v}$ is a subalgebra of $\mathrm{End}(V)$ and that $A_{v}(V)$ is a closed abstract subgroup of $\mathrm{Aut}(V)$. According to Theorem 3.42, $A_{v}(V)$ is a closed Lie subgroup of $\mathrm{Aut}(V)$. Let $a$ be the Lie algebra of $A_{v}(V)$. We need only show that $a = b_{v}$.

If  $ l \in a $, then  $ \exp t l \in A_{\psi}(V) $, so that

 $$ (\mathtt{e x p}t l)\{v,w\}=\{(\mathtt{e x p}t l)(v),(\mathtt{e x p}t l)(w)\}. $$ 

Both sides of (1) are smooth curves in V. Taking their derivatives at t = 0, we obtain

 $$ l\{v,w\}=\{l(v),w\}+\{v,l(w)\}, $$ 

which proves that  $ l \in \mathfrak{b}_{\psi} $. (Observe that a curve  $ \varphi(t) \otimes \psi(t) $ in  $ V \otimes V $ has derivative (or tangent vector) at  $ t = 0 $ equal to  $ \dot{\varphi}(0) \otimes \psi(0) + \varphi(0) \otimes \psi(0) $.)

Conversely, suppose that  $ l \in \mathfrak{b}_{w} $. To prove that  $ l \in \mathfrak{a} $, we need only prove that  $ \exp t l \in A_{w}(V) $ for all  $ t $. We let  $ l \otimes 1 $ denote the endomorphism of  $ V \otimes V $ defined by

 $$ (l\otimes1)(v\otimes w)=l(v)\otimes w. $$ 

The fact that  $  l \in \mathbf{b}_{v}  $ means that

 $$ l\{v,w\}=\{l(v),w\}+\{v,l(w)\} $$ 

for all v and w in V; and this can be expressed as

 $$ l\circ\varphi=\varphi\circ(l\otimes1+1\otimes l). $$ 

It follows from (4) that

 $$ l^{n}\circ\varphi=\varphi\circ(l\otimes1+1\otimes l)^{n}, $$ 

so that

 $$ e^{t l}\circ\psi=\psi\circ e^{t(l\otimes1+1\otimes l)}. $$ 

Now,  $ (l \otimes 1) \circ (1 \otimes l) = (1 \otimes l) \circ (l \otimes 1) $, so we can apply 3.35(9) to the right-hand term in (6). Then, by the fact that  $ e^{t(l \otimes 1)} = e^{t l} \otimes 1 $, equation (6) becomes

 $$ \begin{aligned}{e^{t l}\circ\psi}&{{}=\psi\circ e^{t(i\otimes1)}\circ e^{t(i\otimes l)}=\psi\circ(e^{t l}\otimes1)\circ(1\otimes e^{t l})}\\ {}&{{}=\psi\circ e^{t l}\otimes e^{t l}.}\\ \end{aligned} $$ 

Thus

 $$ (\mathtt{e x p}t l)\{v,w\}=\{(\mathtt{e x p}t l)(v),(\mathtt{e x p}t l)(w)\} $$ 

for all $v$ and $w$ in $V$, which implies that $\exp t l \in A_{\psi}(V)$ for all $t \in \mathbb{R}$. Thus $a = b_{\psi}$, and the theorem is proved.

3.55 Definitions Again we let $V$ be a finite dimensional vector space over a field $F$ where $F$ is either $\mathbb{R}$ or $\mathbb{C}$. A bilinear form $B$ on $V$ is a linear map $B: V \otimes V \to F$. We shall use the notation $B(v \otimes w) = (v, w)$.

(a) We let

 $$ A_{B}(V)=\big\{\alpha\in\operatorname{A u t}(V)\colon(v,w)=\big(\alpha(v),\alpha(w)\big)\mathrm{f o r~a l l~}v,w\in V\big\}. $$ 

The elements of $A_{B}(V)$ are the automorphisms of $V$ which preserve the bilinear form $B$.

(b) We let

 $$ \mathfrak{d}_{B}=\big\{I\in\mathbb{E}\mathrm{e n d}(V)\colon\big(l(v),w\big)+\big(v,l(w)\big)=0\mathrm{f o r~a l l~}v,w\in V\big\}. $$ 

Elements of  $ b_{B} $ are called derivations of the bilinear form B.

3.56 Theorem  $ A_{B}(V) $ is a closed Lie subgroup of  $ \mathrm{Aut}(V) $ with Lie algebra  $ \mathfrak{d}_{B} $.

The proof is similar to the proof of Theorem 3.54, and we leave it to the reader as an exercise.

### 3.57 Applications of 3.54 and 3.56

(a) Let $V$ be a real vector space with an inner product $B$. According to Theorem 3.56, the automorphisms of $V$ which preserve the inner product form a closed Lie subgroup $A_B(V) \subset \mathrm{Aut}(V)$ whose Lie algebra is the Lie subalgebra $\mathfrak{b}_B \subset \mathrm{End}(V)$ of derivations of the inner product $B$. Choose an orthonormal basis for $V$. Now consider the Lie group isomorphism of $\mathrm{Aut}(V)$ with $GI(n, \mathbb{R})$ and the associated Lie algebra isomorphism of $\mathrm{End}(V)$ with $\mathrm{gl}(n, \mathbb{R})$ determined by associating with each linear transformation on $V$ its matrix relative to this basis. It is easily seen that $A_B(V)$ is mapped onto the orthogonal group $O(n) \subset GI(n, \mathbb{R})$ and that $\mathfrak{b}_B$ is mapped onto the set $\mathfrak{o}(n)$ of skew-symmetric matrices in $\mathrm{gl}(n, \mathbb{R})$. This provides another proof of the fact that the orthogonal group $O(n)$ is a closed Lie subgroup of $GI(n, \mathbb{R})$ with Lie algebra $\mathfrak{o}(n)$.

(b) A Lie algebra g has a bilinear operation—the bracket [, ]. The automorphisms of g which preserve the bracket are precisely the Lie algebra isomorphismsof g. We shall denote them by  $ A(g) $. According to 3.54,  $ A(g) $ is a closed Lie subgroup of  $ \mathrm{Aut}(g) $ with Lie algebra the derivations of [, ] which we shall denote by b(g).

Suppose that G is a simply connected Lie group with Lie algebra g. Let  $ A(G) $ be the group of all Lie group automorphisms of G. The map

 $$ \psi\colon A(G)\to A(\mathfrak{g})\quad{\mathrm{d e f i n e d~b y}}\quad\psi(\alpha)=d\alpha $$ 

is a homomorphism and is 1:1 by 3.16 and onto by 3.27. Thus we can induce via $\psi$ a manifold structure on $A(G)$, making $A(G)$ into a Lie group with Lie algebra isomorphic with $\mathfrak{b}(g)$.

##### HOMOGENEOUS MANIFOLDS

3.58 Theorem Let $H$ be a closed subgroup of a Lie group $G$, and let $G|H$ be the set $\{\sigma H: \sigma \in G\}$ of left cosets modulo $H$. Let $\pi: G \to G|H$ denote the natural projection $\pi(\sigma) = \sigma H$. Then $G|H$ has a unique manifold structure such that

(a)  $ \pi $ is  $ C^{\infty} $.

(b) There exist local smooth sections of $G/H$ in $G$; that is, if $\sigma H \in G/H$, there is a neighborhood $W$ of $\sigma H$ and a $C^\infty$ map $\tau: W \to G$ such that $\pi \circ \tau = \mathrm{id}$.

PROOF Existence We topologize $G/H$ by requiring $U$ in $G/H$ to be open if and only if $\pi^{-1}(U)$ is an open set in $G$. With this topology, $\pi$ is an open map since if $W$ is open in $G$, then

 $$ \pi^{-1}\bigl(\pi(W)\bigr)=\bigcup_{h\in H}W h, $$ 

which implies that $\pi(W)$ is open in $G/H$. Moreover, $G/H$ is Hausdorff. To see this, first observe that the set $R \subset G \times G$ consisting of all pairs $(\sigma, \tau)$ for which there exists an $h \in H$ such that $\sigma = \tau h$ is a closed set since $R = \alpha^{-1}(H)$ where $\alpha$ is the continuous map $(\sigma, \tau) \mapsto \tau^{-1}\sigma$ of $G \times G$ into $G$. Now, if $\sigma H$ and $\tau H$ are distinct points of $G/H$, $(\sigma, \tau)$ does not belong to $R$, so there exist open neighborhoods $V$ of $\sigma$ and $W$ of $\tau$ in $G$ such that $(V \times W) \cap R = \varnothing$. Then $\pi(V)$ and $\pi(W)$ are disjoint open neighborhoods of $\sigma H$ and $\tau H$ respectively, which proves that $G/H$ is Hausdorff. A countable basis for the topology on $G$ projects under $\pi$ to a countable basis for the topology on $G/H$. Thus $G/H$ is second countable.

According to 3.42, the closed subgroup $H$ is a Lie subgroup of $G$. Suppose that $G$ is of dimension $d$ and that $H$ is of dimension $d-k$. To prove that $G/H$ is locally Euclidean and to obtain a cover of smoothly overlapping coordinate systems on $G/H$, we first prove that there exists a cubic centered coordinate system $(U,\varphi)$ about $e$ in $G$, with coordinate functions $x_{1},\ldots,x_{d}$, such that distinct slices of the form

 $$ x_{i}=\mathrm{c o n s t a n t}\qquad\mathrm{f o r~a l l~}i\in\{1,\ldots,k\} $$ 

lie on distinct left cosets of $H$. Let $\mathcal{D}$ be the distribution on $G$ determined by the Lie algebra of $H$. Then, by 1.60, there is a cubic centered coordinate system $(V,\varphi)$ about $e$ in $G$, with coordinate functions $x_{1},\ldots,x_{d}$, such that the integral manifolds of $\mathcal{D}$ in $V$ are slices of the form (1). Since $H$ is a closed subgroup of $G$, and therefore as a Lie subgroup has the relative topology, $V$ can be chosen small enough so that

 $$ \bullet \quad \quad V\cap H=\mathrm{t h e~s l i c e~}S_{0}\mathrm{~t h r o u g h~}e. $$ 

Choose neighborhoods U and $V_{1}$ of $e$, cubic relative to the coordinate system $(V,\varphi)$, such that

 $$ V_{1}V_{1}\subset V\qquad\mathrm{a n d}\qquad U^{-1}U\subset V_{1}. $$ 

Now suppose that $\sigma$ and $\tau$ are points of $U$ which lie in the same coset modulo $H$, so $\sigma \in \tau H$. Then

 $$ \tau^{-1}\sigma\in V_{1}\cap H=V_{1}\cap S_{0}. $$ 

So $\sigma \in \tau(V_1 \cap S_0)$. Now $\tau(V_1 \cap S_0)$ is an integral manifold of $\mathcal{D}$ which lies in $V$ by the choice of $V_1$ in (3), and $\tau(V_1 \cap S_0)$ is connected. Therefore $\tau(V_1 \cap S_0)$ lies in a single slice of $V$. So $\sigma$ and $\tau$ lie in the same slice. Conversely, it is easily seen that a single slice lies on a single coset. Thus $(U, \phi)$ is the desired coordinate system.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//2c4fbfc3-1037-4444-a2b3-97b299b84a1b/markdown_0/imgs/img_in_image_box_110_434_764_801.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2Fbcce0d330136c78d53ba00c2edf5068146c2d7ab82b2aae0cc3f16c3ce2c45db" alt="Image" width="68%" /></div>

Let $S$ be the slice of $\varphi(U)$ on which $x_{k+1},\ldots,x_{d}$ vanish. Let $\widetilde{\varphi}^{-1}$ be the map defined by setting

 $$ \tilde{\varphi}^{-1}=\pi\circ\varphi^{-1}\bigm|S\colon S\to\pi(U). $$ 

Then $\tilde{\varphi}^{-1}$ is one-to-one by the choice of the coordinate system $(U,\varphi)$, and is also continuous and an open map; hence it is a homeomorphism. Let $\tilde{\varphi}$ be the inverse,

 $$ \tilde{\varphi}\colon\pi(U)\to S\subset\mathbb{R}^{k}. $$ 

Then $(\pi(U),\tilde{\varphi})$ is a coordinate system about the identity coset in $G/H$. We obtain coordinate systems about other points of $G/H$ by left translations. Indeed, if $\sigma\in G$, we let $l_\sigma$ be the homeomorphism of $G/H$ induced by left translation $l_\sigma$ on $G$; that is,

 $$ \tilde{l}_{o}(\tau H)=\sigma\tau H. $$ 

Then for each $\sigma H \in G/H$ we define a map $\tilde{\varphi}_{\sigma H}$ by setting

 $$ \tilde{\varphi}_{\sigma H}=\tilde{\varphi}\circ\tilde{l}_{\sigma^{-1}}\big|\tilde{l}_{\sigma}\big(\pi(U)\big). $$ 

Then  $ (\tilde{l}_{e}(\pi(U)), \tilde{\varphi}_{eH}) $ is a coordinate system about  $ \sigma H $. Note that in this notation  $ \tilde{\varphi}_{H} $ is just the map  $ \tilde{\varphi} $. Now, we claim that one obtains a differentiable structure on  $ G/H $ by maximizing the collection of coordinate systems

 $$ \big\{\big(\tilde{l}_{\sigma}\big(\pi(U)\big),\tilde{\Phi}_{\sigma H}\big)\colon\sigma\in G\big\}. $$ 

One has only to check differentiability on overlaps. So let  $ (\tilde{l}_{\sigma_{1}}(\pi(U)), \tilde{\varphi}_{\sigma_{1}H}) $ and  $ (\tilde{l}_{\sigma_{2}}(\pi(U)), \tilde{\varphi}_{\sigma_{2}H}) $ be two such coordinate systems, and let

 $$ \begin{array}{r}{\widehat{V}=\tilde{\varphi}_{\sigma_{1}H}(\tilde{l}_{\sigma_{1}}(\pi(U))\cap\tilde{l}_{\sigma_{2}}(\pi(U))).}\end{array} $$ 

We must prove that $\tilde{\varphi}_{\sigma_1H} \circ \tilde{\varphi}_{\sigma_1H}^{-1} \mid V$ is $C^\infty$. Let $t \in V$. Then since $\tilde{l}_{\sigma_1^{-1}} \circ \tilde{l}_{\sigma_1} \circ \tilde{\varphi}^{-1}(t) \in \pi(U)$, there exists an element $g \in H$ such that $\sigma_2^{-1} \sigma_1 \varphi^{-1}(t) g \in U$. It follows that there exists a neighborhood $W$ of $t$ in $V$ such that $\sigma_2^{-1} \sigma_1 \varphi^{-1}(W) g \subset U$. It suffices to prove that $\tilde{\varphi}_{\sigma_1H} \circ \tilde{\varphi}_{\sigma_1H}^{-1} \mid W$ is $C^\infty$. But we can express $\tilde{\varphi}_{\sigma_1H} \circ \tilde{\varphi}_{\sigma_1H}^{-1} \mid W$ as the following composition of $C^\infty$ maps:

 $$ \tilde{\varphi}_{\sigma_{0}H}\circ\tilde{\varphi}_{\sigma_{1}H}^{-1}\mid W=\pi_{0}\circ\varphi\circ r_{g}\circ l_{\sigma_{1}^{-1}\sigma_{1}}\circ\varphi^{-1}\mid W, $$ 

where  $ \pi_0 $ is the canonical projection of  $ \varphi(U) $ onto S. Thus  $ \widetilde{\varphi}_{\sigma_1H} \circ \widetilde{\varphi}_{\sigma_1H}^{-1} \mid V $ is  $ C^\infty $.

With this differentiable structure on $G/H$, the projection $\pi: G \to G/H$ is $C^\infty$; indeed, $\pi$ restricted to an open set of the form $I_e(U)$ is nothing other than the composition $\tilde{\varphi}_{eH}^{-1} \circ \pi_0 \circ \varphi \circ I_{e^{-1}} \mid I_e(U)$. Thus result (a) holds; and as for (b), $I_e \circ \varphi^{-1} \circ \tilde{\varphi}_{eH}$ is a local smooth section of $G/H$ in $G$ on the neighborhood $I_e(\pi(U))$ of $\sigma H$.

Uniqueness Let  $ (G/H)_{1} $ denote G/H with another differentiable structure satisfying (a) and (b).

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//2c4fbfc3-1037-4444-a2b3-97b299b84a1b/markdown_1/imgs/img_in_image_box_319_852_565_987.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A14Z%2F-1%2F%2F58cf94eba2c7393914c1165a4eedef7e3df15aacaca5971046308c423641a5e5" alt="Image" width="25%" /></div>

Then the identity map and its inverse are both $C^{\infty}$ since locally they can be expressed as the composition of local smooth sections into $G$ followed by $\pi$. Thus id is a diffeomorphism, which proves uniqueness.

3.59 Definition Manifolds of the form $G/H$ where $G$ is a Lie group, $H$ is a closed subgroup of $G$, and the manifold structure is the unique one satisfying (a) and (b) of Theorem 3.58 are called homogeneous manifolds.

3.60 Remark Observe that $f$ is a $C^{\infty}$ function on $G/H$ if and only if $f\circ\pi$ is a $C^{\infty}$ function on $G$; for if $f$ is $C^{\infty}$, then certainly $f\circ\pi$ is $C^{\infty}$. Conversely if $f\circ\pi$ is $C^{\infty}$, then $f$, which can locally be represented as the composition of a smooth section of $G/H$ in $G$ with $f\circ\pi$, is also $C^{\infty}$.

### 3.61 Definitions Let

 $$ \eta\colon G\times M\to M $$ 

be an action of G on M on the left (cf. 3.44); and, as usual, let

 $$ \eta_{\sigma}(m)=\eta(\sigma,m). $$ 

The action is called effective if $e$ is the only element of $G$ for which $\eta_{e}$ is the identity map on $M$. The action is called transitive if whenever $m$ and $n$ belong to $M$ there exists a $\sigma$ in $G$ such that $\eta_{e}(m) = n$. Let $m_{0} \in M$, and let

 $$ H=\{\sigma\in G\colon\eta_{\sigma}(m_{0})=m_{0}\}. $$ 

H is a closed subgroup of G called the isotropy group at  $ m_{0} $. The action  $ \eta $ restricted to H gives an action of H on M on the left with a fixed point  $ m_{0} $, so by 3.45 we have a representation

 $$ \alpha\colon H\to\operatorname{A u t}(M_{m_{0}})\quad\mathrm{w h e r e}\quad\alpha(\sigma)=d\eta_{\sigma}\left\vert\right.M_{m_{0}}. $$ 

The group  $ \alpha(H) $ of linear transformations of  $ M_{m_{0}} $ is called the linear isotropy group at  $ m_{0} $.

3.62 Theorem Let $\eta: G \times M \to M$ be a transitive action of the Lie group $G$ on the manifold $M$ on the left. Let $m_0 \in M$, and let $H$ be the isotropy group at $m_0$. Define a mapping

 $$ \tilde{\beta}\colon G/H\to M\quad\mathrm{b y}\quad\tilde{\beta}(\sigma H)=\eta_{\sigma}(m_{0}). $$ 

Then  $ \beta $ is a diffeomorphism.

PROOF Observe first that $\tilde{\beta}$ is well-defined since $\eta_{\sigma h}(m_0) = \eta_\sigma(\eta_h(m_0)) = \eta_\sigma(m_0)$ for any $h \in H$. $\tilde{\beta}$ is surjective since $G$ acts transitively, and is injective since if $\tilde{\beta}(\sigma H) = \tilde{\beta}(\tau H)$, then $\eta_{\tau^{-1}\sigma}(m_0) = m_0$, which implies that $\tau^{-1}\sigma$ belongs to $H$, or in other words that $\sigma H = \tau H$. In view of Exercise 6 of Chapter 1, it suffices to prove that $\tilde{\beta}$ is $C^\infty$ and that $d\tilde{\beta}$ is non-singular at each point.

According to Remark 3.60, $\beta$ is $C^{\infty}$ if and only if $\beta\circ\pi$ is $C^{\infty}$ where $\pi$ is the natural projection of $G$ onto $G/H$. But

 $$ \beta\circ\pi=\eta\circ i_{m_{0}} $$ 

where  $ i_{m} $ is the  $ C^{\infty} $ map of G into  $ G \times M $ defined by

 $$ i_{m_{0}}(\sigma)=(\sigma,m_{0}). $$ 

Thus  $ \beta $ is  $ C^{\infty} $.

Now let $\beta=\tilde{\beta}\circ\pi$. Since the kernel of $d\pi\mid G_{\sigma}$ is $(\sigma H)_{\sigma}\subset G_{\sigma}$, in order to prove that $d\tilde{\beta}\mid(G/H)_{\sigma H}$ is non-singular it is sufficient to prove that the kernel of $d\beta\mid G_{\sigma}$ is also $(\sigma H)_{\sigma}$. Since for each $\sigma\in G$,

 $$ \beta=\eta_{e}\circ\dot{\beta}\circ\dot{I}_{e^{-1}}, $$ 

it suffices to prove that the kernel of $d\beta \big| G_\theta$ is $H_\theta$. Certainly $H_\theta \subset \ker(d\beta \big| G_\theta)$. So let $x \in \ker(d\beta \big| G_\theta)$. To show that $x \in H_\theta$, we need only prove that $\exp tX \in H$ for all $t \in \mathbb{R}$ where $X$ is the left invariant vector field on $G$ determined by $x$. For this, it is sufficient to prove that the tangent vector to the curve $t \mapsto \beta(\exp tX)$ in $M$ is identically zero, for then $\beta(\exp tX) \equiv m_\theta$, which implies that $\exp tX \in H$ for all $t$. The tangent vector to this curve at $t$ is

 $$ \begin{aligned}{d\beta(X_{\operatorname{e x p}t\mathbf{X}})}&{{}=d\big(\eta_{\operatorname{e x p}t\mathbf{X}}\circ\beta\circ I_{\operatorname{e x p}(-t\mathbf{X})}\big)\big(X_{\operatorname{e x p}t\mathbf{X}}\big)}\\ {}&{{}=d\eta_{\operatorname{e x p}t\mathbf{X}}\circ d\beta\big(X(e)\big)=d\eta_{\operatorname{e x p}t\mathbf{X}}\circ d\beta(x)=0.}\\ \end{aligned} $$ 

Thus $d\tilde{\beta}$ is everywhere non-singular, and the theorem is proved.

3.63 Remarks If $G$ is a Lie group and $H$ a closed subgroup of $G$, then there is a natural action $\tilde{I}$ of $G$ on the homogeneous manifold $G/H$ on the left, namely,

 $$ \tilde{l}\colon G\times G/H\to G/H,\qquad\tilde{l}(\sigma,\tau H)\stackrel{,}{=}\sigma\tau H. $$ 

It is easily checked that $\tilde{I}$ is $C^{\infty}$ and indeed gives an action of $G$ on $G/H$ on the left. Moreover, it is obvious that $\tilde{I}$ is a transitive action. Now, for each $\sigma$ in $G$, $\tilde{I}_{e}$ (notation as in 3.61(2)) is a diffeomorphism of $G/H$; and given any two points $\tau H$ and $\gamma H$ of $G/H$ there is a diffeomorphism $\tilde{I}_{\tau\gamma^{-1}}$ taking $\gamma H$ to $\tau H$. The reason that manifolds of the form $G/H$ are called homogeneous is that they possess this transitive group of diffeomorphisms. Conversely, Theorem 3.62 shows that if a manifold $M$ has a transitive group of diffeomorphisms in the sense of 3.61(1), then $M$ is diffeomorphic with a homogeneous manifold $G/H$.

From Theorem 3.62 we get another characterization of the manifold structure on $G/H$, namely, the set $G/H$ has a unique manifold structure such that the natural map (1) is $C^{\infty}$.

3.64 Theorem Let G be a Lie group and H a closed normal subgroup of G. Then the homogeneous manifold G/H with its natural group structure is a Lie group.

PROOF One has only to check that the map

 $$ (\sigma H,\tau H)\mapsto\sigma\tau^{-1}H $$ 

of $G/H \times G/H \to G/H$ is $C^{\infty}$. Let $\alpha_{e}: W_{e} \to G$ and $\alpha_{r}: W_{r} \to G$ be local sections of $G/H$ in $G$ on neighborhoods $W_{e}$ of $\sigma H$ and $W_{r}$ of $\tau H$

respectively. Then locally the map (1) can be expressed as the following composition of $C^{\infty}$ maps:

 $$ \pi\circ\varphi\circ(\alpha_{e}\times\alpha_{r}), $$ 

where  $ \varphi: G \times G \to G $ is the map  $ \varphi(\sigma, \tau) = \sigma\tau^{-1} $.

### 3.65 Examples of homogeneous manifolds

(a) Let $\{e_i: i = 1, \ldots, n\}$ be the canonical basis of $\mathbb{R}^n$ where $e_i$ is the $n$-tuple consisting of all zeros except for a 1 in the $i$th spot. Each matrix $\sigma \in G l(n, \mathbb{R})$ uniquely determines a linear transformation on $\mathbb{R}^n$, which we shall also denote by $\sigma$, by requiring that

(1)

 $$ \sigma(e_{j})=\sum_{i}\sigma_{i j}e_{i}. $$ 

In other words, if we consider the $n$-tuples of $\mathbb{R}^n$ as $n \times 1$ matrices, then $\sigma$ acts on $\mathbb{R}^n$ in the natural way by matrix multiplication. The map $(\sigma, v) \mapsto \sigma(v)$ gives an action of $Gl(n, \mathbb{R})$ on $\mathbb{R}^n$ on the left:

 $$ G l(n,\mathbb{R})\times\mathbb{R}^{n}\to\mathbb{R}^{n}. $$ 

Let  $ \langle\quad,\quad\rangle $ denote the standard inner product on  $ \mathbb{R}^n $ with respect to which the basis  $ \{e_i\} $ is orthonormal. Then if  $ \sigma\in G l(n,\mathbb{R}) $,

 $$ \langle\sigma(v),w\rangle=\langle v,\sigma^{t}(w)\rangle. $$ 

If  $ \sigma \in O(n) $, then  $ \sigma^t \sigma = I $, so it follows from (3) that

 $$ \langle\sigma(v),\sigma(v)\rangle=\langle v,\sigma^{t}\sigma(v)\rangle=\langle v,v\rangle; $$ 

thus $\sigma$ preserves lengths of vectors. Thus the action (2) restricted to $O(n) \times S^{n-1}$ factors through the unit sphere $S^{n-1}$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//6cc4845f-bbd3-4ae5-98d8-9e81fb995a7e/markdown_0/imgs/img_in_image_box_341_806_657_927.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2F5ca098b3406897a1ae0ffc87786955b0d83fc9492832222667a1beca1b9a3571" alt="Image" width="33%" /></div>

According to 1.32, the factoring map is smooth, so we have a natural  $ C^{\infty} $ action

 $$ O(n)\times S^{n-1}\to S^{n-1} $$ 

of the orthogonal group $O(n)$ on the unit sphere $S^{n-1}$ on the left. We claim that the action (6) is transitive. If $v_1 \in S^{n-1}$, let $\{v_1, v_2, \ldots, v_n\}$ be an orthonormal basis of $\mathbb{R}^n$ containing $v_1$ as the first element. Let

 $$ v_{i}=\sum_{j}\sigma_{j i}e_{j}. $$ 

Then the matrix  $ \sigma $ whose entries are determined by (7) is orthogonal, and

 $$ \sigma(e_{1})=v_{1}. $$ 

It follows that if v and w are any two points of  $ S^{n-1} $, there is an orthogonal matrix  $ \sigma $ such that  $ \sigma(v) = w $. Thus the action (6) is transitive.

The set of matrices in  $ O(n) $ of the form

 $$ \begin{array}{r l}{\sigma=}&{{}\left(\left(\begin{array}{l l l}{}&{}&{0}\\ {\bar{\sigma}}&{}&{}\end{array}\right)\begin{array}{l}{.}\\ {.}\\ {.}\end{array}\right)}\\ {}&{{}\left(\begin{array}{l l l}{0}&{\cdots}&{0}\\ \end{array}\right.\left.\begin{array}{l}{1}\\ {1}\end{array}\right)}\end{array} $$ 

forms a closed subgroup of $O(n)$. The matrices $\tilde{\sigma}$ occurring in this subgroup are precisely the matrices in $O(n-1)$. So $O(n-1)$ sits in $O(n)$ as this natural closed subgroup. We claim that $O(n-1)$ is precisely the isotropy group for the action (6) at $e_n\in S^{n-1}$. Clearly the elements of $O(n-1)$ leave $e_n$ fixed. On the other hand, suppose that $\sigma\in O(n)$ and that $\sigma(e_n)=e_n$. Now

 $$ \sigma(e_{n})=\sum_{i}\sigma_{i n}e_{i}, $$ 

so  $ \sigma_{in}=0 $ for  $ i<n $ and  $ \sigma_{nn}=1 $. Since  $ \sigma $ is orthogonal,  $ \sigma\sigma^{t}=I $, and this implies that  $ \sum\sigma_{ni}^{2}=1 $. Since  $ \sigma_{nn}=1 $, we must have  $ \sigma_{ni}=0 $,  $ i<n $. Thus  $ \sigma\in O(n-1) $. It follows from Theorem 3.62 that the map

 $$ O(n)/O(n-1)\to S^{n-1},\qquad\sigma O(n-1)\mapsto\sigma(e_{n}) $$ 

is a diffeomorphism. Thus the sphere  $ S^{n-1} $ is in a natural way diffeomorphic with the homogeneous manifold  $ O(n)/O(n-1) $.

By a similar argument one can show that there is a diffeomorphism of the sphere  $ S^{n-1} $ with the homogeneous manifold  $ \mathrm{SO}(n)/\mathrm{SO}(n-1) $.

(b) Let $\{e_t: i = 1, \ldots, n\}$ be the canonical complex basis of $\mathbb{C}^n$ where $e_t$ is the $n$-tuple consisting of all zeros except for a 1 in the $i$th spot. Just as in Example (a), each matrix $\sigma \in G/(n, \mathbb{C})$ uniquely determines a linear transformation of $\mathbb{C}^n$, which we still denote by $\sigma$, by requiring

 $$ \sigma(e_{j})=\sum_{i}\sigma_{i j}e_{i}. $$ 

So if we consider the complex $n$-tuples of $\mathbb{C}^*$ as $n \times 1$ matrices, then $\sigma$ acts by matrix multiplication. The map $(\sigma, v) \mapsto \sigma(v)$ is an action of

the real $2n^{8}$-dimensional Lie group $GI(n,\mathbb{C})$ on the real $2n$-dimensional manifold $\mathbb{C}^{*}$ on the left:

 $$ G l(n,\mathbb{C})\times\mathbb{C}^{n}\to\mathbb{C}^{n}. $$ 

Let  $ \langle $ ,  $ \rangle $ denote the standard inner product on  $ C^{*} $, where

 $$ \left\langle\sum_{i}a_{i}e_{i},\sum_{i}b_{i}e_{i}\right\rangle=\sum_{i=1}^{n}a_{i}\bar{b}_{i}. $$ 

Then if  $ \sigma \in Gl(n, \mathbb{C}) $,

 $$ \langle\sigma(v),w\rangle=\langle v,\bar{\sigma}^{t}(w)\rangle. $$ 

If $\sigma$ is an element of the unitary group $U(n)$, then $\bar{\sigma}^{i}\sigma = I$, so it follows from (14) that $\sigma$ preserves lengths of vectors in $\mathbb{C}^{n}$. If $X$ denotes the unit sphere in $\mathbb{C}^{n}$, then the action (12) restricted to $U(n) \times X$ factors through $X$, and so, by 1.32, yields a $C^{\infty}$ action

 $$ U(n)\times X\to X $$ 

of the unitary group $U(n)$ on the unit sphere $X \subset \mathbb{C}^*$ on the left. It follows by an argument similar to that in Example (a) that the action (15) is transitive and that the isotropy group for the action (15) at the point $e_n$ is simply $U(n-1)$, which we consider to be a closed subgroup of $U(n)$ by identifying $\tilde{\sigma} \in U(n-1)$ with

 $$ \begin{array}{r l}{\sigma=}&{{}\left(\left(\begin{array}{l l l}{}&{}&{0}\\ {}&{\tilde{\sigma}}&{}\end{array}\right)\begin{array}{l}{.}\\ {.}\\ {.}\end{array}\right)}\\ {}&{{}\left(\begin{array}{l l l}{0}&{\cdots}&{0}\\ {}&{1}&{}\end{array}\right)}\end{array} $$ 

in $U(n)$. Thus, by 3.62, $X$ is diffeomorphic with the homogeneous manifold $U(n)/U(n-1)$. But now under the canonical global coordinate system on $\mathbb{C}^n$ (given by the dual basis to the real basis $\{e_1, \ldots, e_n, \sqrt{-1}e_1, \ldots, \sqrt{-1}e_n\}$ of $\mathbb{C}^n$), $X$ is diffeomorphic with $S^{2n-1} \subset \mathbb{R}^{2n}$. Thus the sphere $S^{2n-1}$ is diffeomorphic with the homogeneous manifold $U(n)/U(n-1)$.

By a similar argument, the sphere $S^{2n-1}$ is also diffeomorphic with the homogeneous manifold $SU(n)/SU(n-1)$. In particular, since $SU(1)$ consists only of the $1\times1$ identity matrix, $S^{2}$ is diffeomorphic with $SU(2)$. Thus $S^{3}$ can be given a Lie group structure. It can be shown that $S^{1}$ and $S^{3}$ are the only spheres possessing Lie group structures [25].

(c) The real projective space  $ P^{n-1} $ is the set of equivalence classes of points in  $ \mathbb{R}^n - \{0\} $ where  $ (a_1, \ldots, a_n) $ is equivalent to  $ (b_1, \ldots, b_n) $ if there is a non-zero real number  $ c $ such that  $ ca_i = b_i $ for  $ i = 1, \ldots, n $. If  $ P^{n-1} $ is given the largest topology in which the natural projection

 $$ \pi\colon(\mathbb{R}^{n}-\{0\})\to P^{n-1} $$ 

is continuous, then $\pi$ restricted to $S^{n-1}$ is a 2-fold covering of $P^{n-1}$, and it is easily established that $P^{n-1}$ has a unique differentiable structure such that this covering map is locally a diffeomorphism. By an argument similar to that in Example (a), one can show that $P^{n-1}$ is diffeomorphic with the homogeneous space $SO(n)/O(n-1)$, where we consider $O(n-1)$ as a closed subgroup of $SO(n)$ by identifying $\tilde{\sigma}\in O(n-1)$ with the following element $\sigma$ of $SO(n)$:

 $$ \sigma=\left(\left(\begin{array}{c c c}{}&{}&{0}\\ {}&{\tilde{\sigma}}&{}\\ {}&{}&{}\\ {0}&{\cdots}&{0}&{\operatorname*{d e t}\tilde{\sigma}}\\ \end{array}\right)\right. $$ 

(d) As a set, the complex projective space $CP^{n-1}$ is the set of equivalence classes of points of $C^{n}-\{0\}$ under the equivalence relation in which $(\alpha_{1},\ldots,\alpha_{n})$ is equivalent to $(\beta_{1},\ldots,\beta_{n})$ if there is a non-zero complex number $\gamma$ such that $\gamma\alpha_{i}=\beta_{i}$ for $i=1,\ldots,n$. We make $CP^{n-1}$ into a real $2(n-1)$ dimensional manifold as follows. The action of the special unitary group on the unit sphere in $C^{n}$ preserves these equivalence classes, and each element of $CP^{n-1}$ has representatives of unit length; thus we have a natural transitive action of $SU(n)$ on the set $CP^{n-1}$:

 $$ S U(n)\times\mathbb{C}P^{n-1}\to\mathbb{C}P^{n-1}. $$ 

The subgroup of $SU(n)$ leaving fixed the point of $\mathbb{C}P^{n-1}$ determined by $e_n \in \mathbb{C}^n$ is simply $U(n-1)$, which we consider to be a closed subgroup of $SU(n)$ by identifying $\tilde{\sigma} \in U(n-1)$ with

 $$ \sigma=\left(\begin{matrix}{\left(\begin{array}{c}{\tilde{\sigma}}\\ {\phantom{0}}\\ \end{array}\right)}&{\left(\begin{array}{c}{0}\\ {\cdot}\\ {\cdot}\\ {\cdot}\\ {0}\\ \end{array}\right)}\\ {0}&{\cdots}&{0}&{1/(\operatorname*{d e t}\tilde{\sigma})}\\ \end{matrix}\right). $$ 

in SU(n). It follows that the map

 $$ \sigma U(n-1)\mapsto\{\sigma(e_{n})\}, $$ 

where $\{\sigma(e_n)\}$ denotes the point of $CP^{n-1}$ determined by $\sigma(e_n)$, is a well-defined one-to-one map of $SU(n)/U(n-1)$ onto $CP^{n-1}$. We give $CP^{n-1}$ the structure of a real $2(n-1)$ dimensional manifold by requiring that the map (19) be a diffeomorphism.

(e) Let $V$ be a real $d$-dimensional vector space, and let $S_{s}(V)$ be the set of $p$-frames in $V$. That is,

 $$ S_{p}(V)=\{\tilde{w}=(w_{1},\ldots,w_{p})\colon\mathrm{t h e}w_{1},\ldots,w_{p} $$ 

are linearly independent elements of $V$.

If we choose a basis $v_{1}, \ldots, v_{d}$ for $V$, then $Gl(d,\mathbb{R})$ acts on $V$ by matrix multiplication. We define

 $$ \eta\colon G l(d,\mathbb{R})\times S_{g}(V)\to S_{g}(V) $$ 

 $$ \begin{array}{r l}{\mathrm{b y}}&{\eta\big(\sigma,(w_{1},\ldots,w_{p})\big)=\big(\sigma(w_{1}),\ldots,\sigma(w_{p})\big).}\end{array} $$ 

Observe that if $\tilde{v}$, $\tilde{w} \in S_p(V)$, then there is a $\sigma \in G l(d, \mathbb{R})$ such that $\eta(\sigma, \tilde{v}) = \tilde{w}$. Now let $\tilde{s}$ be the element of $S_p(V)$ determined by the first $p$ elements of the basis $v_1, \ldots, v_d$; hence $\tilde{s} = (v_1, \ldots, v_p)$. Let $H$ be the subset of $Gl(d, \mathbb{R})$ leaving $\tilde{s}$ fixed. Then

 $$ H=\Big\{\left(\frac{I}{O}\left|\frac{A}{B}\right.\right)\in{G l}(d,\mathbb{R})\Big\}, $$ 

where $I$ is the $p \times p$ identity matrix; thus $H$ is a closed subgroup of $Gl(d,\mathbb{R})$. It follows that the map $\sigma H \mapsto \eta(\sigma,\tilde{s})$ is a one-to-one map of the homogeneous manifold $Gl(d,\mathbb{R})/H$ onto the set $S_p(V)$. We give $S_p(V)$ the structure of a $d \cdot p$-dimensional manifold by requiring that this map be a diffeomorphism. It is easily checked that this manifold structure is independent of the basis of $V$ chosen. $S_p(V)$ is called the Stiefel manifold of $p$-frames in $V$.

(f) Again let $V$ be a real $d$-dimensional vector space, and now let $M_{k}(V)$ be the set of all $k$-dimensional subspaces $(k$-planes) of $V$. If we choose a basis $v_{1}, \ldots, v_{d}$ for $V$, then the orthogonal group $O(d)$ acts naturally on $V$ by matrix multiplication; and since non-singular linear transformations map $k$-planes to $k$-planes, we have a map

 $$ \eta\colon O(d)\times M_{k}(V)\to M_{k}(V). $$ 

Observe that if $P$ and $Q$ are $k$-planes, then there is a $\sigma \in O(d)$ such that $\eta(\sigma,P) = Q$. Now, let $P_0$ be the $k$-plane spanned by the first $k$ elements of the basis $v_1, \ldots, v_d$, and let $H$ be the subset of $O(d)$ leaving $P_0$ fixed. Then

 $$ H=\Big\{\left(\frac{\sigma}{0}\Big|\frac{0}{\tau}\right)\in O(d)\colon\sigma\in O(k),\;\tau\in O(d-k)\Big\}, $$ 

so $H$ is a closed subgroup of $O(d)$ which we can identify with $O(k) \times O(d-k)$. Then the map $\sigma(O(k) \times O(d-k)) \mapsto \eta(\sigma, P_0)$ is a one-to-one map of the homogeneous manifold $O(d)/[O(k) \times O(d-k)]$ onto the set $M_k(V)$. We make $M_k(V)$ into a $(d-k)k$ dimensional manifold by requiring that this map be a diffeomorphism. One can check that this manifold structure on $M_k(V)$ is independent of the basis chosen for $V$. $M_k(V)$ is known as the Grassmann manifold of $k$-planes in $V$.

3.66 Proposition Let H be a closed subgroup of the Lie group G. If H and G/H are connected, then G is connected.

PROOF Assume that

where U and V are non-empty open subsets of G. Then

 $$ G=U\cup V $$ 

where $\pi(U)$ and $\pi(V)$ are non-empty open subsets of $G/H$. Since $G/H$ is connected, there must be a point $\sigma H$ of $G/H$ such that

 $$ G/H=\pi(U)\cup\pi(V) $$ 

 $$ \sigma H\in\pi(U)\cap\pi(V). $$ 

Now, (1) implies that

 $$ \sigma H=(\sigma H\cap U)\cup(\sigma H\cap V) $$ 

where $(\sigma H \cap U)$ and $(\sigma H \cap V)$ are both open subsets of $\sigma H$ (since $H$ has the relative topology). According to (3), both $(\sigma H \cap U)$ and $(\sigma H \cap V)$ are non-empty; thus, since $\sigma H$ is homeomorphic with $H$ and therefore connected, we have

 $$ (\sigma H\cap U)\cap(\sigma H\cap V)\neq\varnothing, $$ 

which implies that

 $$ U\cap V\neq\varnothing, $$ 

which proves that G is connected.

3.67 Theorem Each of the Lie groups $SO(n)$, $SU(n)$, and $U(n)$ is connected for $n\geq1$, and $O(n)$ has two components ($n\geq1$).

PROOF SO(1) and SU(1) are connected since they both consist only of the  $ 1 \times 1 $ identity matrix, and U(1) is connected since

 $$ U(1)=\{(\lambda)\colon\lambda\in\mathbb{C},|\lambda|=1\}. $$ 

That $SO(n)$, $SU(n)$, and $U(n)$ are connected for all $n$ now follows from 3.66 by using induction on $n$ and the representation of spheres as homogeneous manifolds given in 3.65.

Since every matrix in $O(n)$ has determinant $\pm1$, the orthogonal group can be written as the following union of two non-empty disjoint connected open subsets:

 $$ \begin{array}{l}{O(n)=S O(n)\cup\sigma S O(n)\quad\mathrm{w h e r e}\quad\sigma=\left(\begin{matrix}{-1}&{}&{}&{0}\\ {}&{1}&{}&{}\\ {}&{}&{\cdot}&{}\\ {}&{}&{}&{\cdot}\\ {}&{}&{}&{\cdot}\\ {0}&{}&{}&{1}\\ \end{matrix}\right)}\\ {\mathrm{T h u s~}O(n)\mathrm{~h a s~t w o~c o m p o n e n t s.}}\\ \end{array} $$ 

### 3.68 Theorem  $ Gl(n,\mathbb{R}) $ has two components.

PROOF Let $GI(n,\mathbb{R})^{+}$ be the subset of $GI(n,\mathbb{R})$ consisting of matrices with positive determinant, and let $GI(n,\mathbb{R})^{-}$ be the subset consisting of matrices with negative determinant. $GI(n,\mathbb{R})^{+}$ and $GI(n,\mathbb{R})^{-}$ are disjoint homeomorphic open subsets of $GI(n,\mathbb{R})$, so it suffices to prove that $GI(n,\mathbb{R})^{+}$ is connected. To do this, we shall show that each element of $GI(n,\mathbb{R})^{+}$ can be joined to the identity matrix by a continuous curve.

First we show that each element of $Gl(n, \mathbb{R})$ has a polar decomposition; that is, each matrix $\sigma \in Gl(n, \mathbb{R})$ can be expressed in the form

 $$ \sigma=P R $$ 

where $P$ is a positive definite symmetric matrix and $R \in O(n)$. (Recall that all the eigenvalues of a symmetric matrix are real, and that a symmetric matrix is positive definite if each of its eigenvalues is strictly positive.) Since $(\sigma\sigma^t)^t = \sigma\sigma^t$, $\sigma\sigma^t$ is symmetric. Let $a$ be an eigenvalue of $\sigma\sigma^t$ with eigenvector $v \in \mathbb{R}^*$. Then, according to 3.65(3), if $\langle \cdot, \rangle$ denotes the standard inner product in $\mathbb{R}^*$,

 $$ a\langle v,v\rangle=\langle\sigma\sigma^{t}(v),v\rangle=\langle\sigma^{t}(v),\sigma^{t}(v)\rangle. $$ 

Consequently, $a \geq 0$, and since $\sigma\sigma^t$ is non-singular, we must have $a > 0$. Thus $\sigma\sigma^t$ is a positive definite symmetric matrix. Since $\sigma\sigma^t$ is symmetric, there exists an orthogonal matrix $\beta \in O(n)$ such that the matrix

 $$ \beta\sigma\sigma^{\dagger}\beta^{\dagger} $$ 

is diagonal (cf. Exercise 22(a)). Since the eigenvalues of $\sigma\sigma^{t}$ are all positive, the matrix (2) has a square root

 $$ (\beta\sigma\sigma^{t}\beta^{t})^{1/2}; $$ 

that is, (3) is a diagonal matrix, and each diagonal entry is the positive square root of the corresponding entry in the matrix (2). Let

 $$ P=\beta^{t}(\beta\sigma\sigma^{t}\beta^{t})^{\mathbf{1}/2}\beta, $$ 

and let

 $$ R=P^{-1}\sigma. $$ 

P is a positive definite symmetric matrix, and R is orthogonal since (4) implies that  $ P^{2} = \sigma\sigma^{t} $ and therefore that

 $$ \begin{aligned}{R R^{t}}&{{}=P^{-1}\sigma\sigma^{t}(P^{-1})^{t}=P^{-1}\sigma\sigma^{t}(P^{t})^{-1}}\\ {}&{{}=P^{-1}\sigma\sigma^{t}P^{-1}=P^{-1}P P P^{-1}=I.}\\ \end{aligned} $$ 

Thus  $ \sigma = PR $, as we asserted in (1).

If $\sigma \in G l(n, \mathbb{R})^+$, then $\sigma$ has a polar decomposition (1), where now $R$ must have positive determinant; thus $R \in SO(n)$. Let

 $$ P_{t}=t I+(1-t)P $$ 

for $t \in [0,1]$. Then $P_t$ is positive definite for each $t$, so the path $t \mapsto P_tR$ is a continuous curve in $Gl(n,\mathbb{R})^+$ joining $\sigma$ to $R$. Since $SO(n)$ is connected, and therefore pathwise connected, $R$ can be joined to the identity matrix $I$ by a continuous curve. Thus $Gl(n,\mathbb{R})^+$ is pathwise connected, which completes the proof that $Gl(n,\mathbb{R})$ has two components.

##### EXERCISES

1 Prove that a connected Lie group is automatically second countable; that is, the assumption of second countability in the definition of connected Lie group is redundant.

2 Show that the examples in 3.3 are Lie groups.

3 Prove that the examples in 3.5 are Lie algebras.

4 Supply a proof for Proposition 3.12.

5 Prove the necessity of the connectedness assumption in 3.16.

6 Let $\mathcal{I}$ be an ideal of forms on $G^{c}$ generated by a collection $\{\omega_{1},\ldots,\omega_{c-d}\}$ of independent left invariant 1-forms. Let $\mathfrak{h}\subseteq\mathfrak{g}$ be the $d$-dimensional subspace of the Lie algebra of $G$ annihilated by the $\omega_{i}$ ($i=1,\ldots,c-d$). Prove that $\mathfrak{h}$ is a subalgebra of $\mathfrak{g}$ if and only if $\mathcal{I}$ is a differential ideal.

7 In this exercise we outline the proof of Theorem 3.23.

(a) Let $\pi\colon (X,x_0)\to(Y,y_0)$ be a covering, and let $\alpha\colon (Z,z_0)\to(Y,y_0)$ be a continuous map where $Z$ is pathwise and locally pathwise connected, and where $a_\ast(\pi_1(Z,z_0))\subset\pi_\ast(\pi_1(X,x_0))$. Prove that there is a unique continuous map $\tilde{\alpha}\colon(Z,z_0)\to(X,x_0)$ such that $\pi\circ\tilde{\alpha}=\alpha$.

(Sketch: First prove part (a) for the case in which $Z$ is the unit rectangle $[0,1] \times [0,1]$ and $z_0 = (0,0)$. Here the condition on the fundamental groups is trivially satisfied, and the proof follows by partitioning the unit rectangle fine enough so that each subrectangle of the partition maps under $\alpha$ into an evenly covered set in $Y$. As a particular application of this case, it follows that each path in $Y$ has a unique lift to $X$ once base points are chosen.

For the general case, define the lifting $\tilde{\alpha}$ of $\alpha$ as follows. Let $z \in Z$, and let $\gamma: [0,1] \to Z$ be a path joining $z_0$ to $z$; thus $\gamma(0) = z_0$ and $\gamma(1) = z$. Then $\alpha \circ \gamma$ has a unique lift $\tilde{\gamma}$ to $X$ such that $\tilde{\gamma}(0) = x_0$. Set $\tilde{\alpha}(z) = \tilde{\gamma}(1)$. Now use the condition on the fundamental groups and the unique lifting property already established for rectangles to show that $\tilde{\alpha}$ is well-defined, independent of the choice of the path $\gamma$ from $z_0$ to $z$. Finally use the local path-connected property of $Z$ to show that $\tilde{\alpha}$ is continuous.)

(b) If $X$ is a pathwise connected, locally pathwise connected, and semi-locally 1-connected topological space, then $X$ has a simply connected covering space.

(Sketch: Fix a base point $x_0 \in X$. We define an equivalence relation on the set of all paths in $X$ with domain [0,1] and with initial point $x_0$. Two such paths $\gamma_1$, $\gamma_2$ will be called equivalent if $\gamma_1(1) = \gamma_2(1)$, and the loop $\gamma_2^{-1}\gamma_1$ at $x_0$ obtained by first traversing $\gamma_1$ and then traversing $\gamma_2$ in the reverse direction is homotopically trivial at $x_0$. The point set of the simply connected covering space $\tilde{X}$ of $X$ is the set of such equivalence classes $\{\gamma\}$. The projection map $\pi: \tilde{X} \to X$ is defined by $\pi(\{\gamma\}) = \gamma(1)$. Let $\{\gamma\} \in \tilde{X}$, and let $U$ be an open neighborhood of $\gamma(1)$ in $X$. Let $U(\{\gamma\})$ consist of all elements $\{\tau\}$ of $\tilde{X}$ possessing a representative path $\tau$ which first traverses $\gamma$ and then remains in $U$. Prove that the collection of such sets $U(\{\gamma\})$ forms a basis for a topology on $\tilde{X}$ in which $\tilde{X}$ is simply connected, and in which $\pi: \tilde{X} \to X$ becomes a covering.)

(c) A covering of a simply connected space is a homeomorphism. (This is an immediate application of part (a).)

8 Prove that if $\pi: \tilde{M} \to M$ is a covering of a differentiable manifold $M$, then $\tilde{M}$ is second countable. (It suffices to prove that $\pi_{1}(M, m)$ is countable. This follows easily from the observation that $M$ can be covered by a countable number of open sets, each homeomorphic with an open ball in Euclidean space.)

9 Let $G$ and $H$ be Lie groups with $G$ connected. Prove that a $C^{\infty}$ map $\varphi: G \to H$ sending the identity of $G$ to the identity of $H$ is a homomorphism if $\delta\varphi$ pulls left invariant forms on $H$ back to left invariant forms on $G$. Show that the assumption of connectedness for $G$ is necessary. (Hint: One can construct a differential ideal on $G \times H$ as in 3.15(5) whose maximal connected integral submanifold $I$ through $(e,e)$ is a Lie subgroup of $G \times H$. Factor the graph of $\varphi$ through $I$, and show that the natural covering homomorphism of $I$ onto $G$ is 1:1.)

10 Prove that  $ \begin{pmatrix}-2 & 0 \\ 0 & -1\end{pmatrix} $ is not  $ e^A $ for any  $ A \in \mathrm{gl}(2, \mathbb{R}) $.

11 Let  $ \sigma(t) $ and  $ \beta(t) $ be smooth curves in a Lie group G such that  $ \sigma(0) = \beta(0) = e $, and let  $ \alpha(t) = \sigma(t)\beta(t) $. Prove that

 $$ \dot{\alpha}(0)=\dot{\sigma}(0)+\dot{\beta}(0). $$ 

(Hint: Consider the group multiplication map  $ \eta\colon G\times G\to G $, that is,  $ \eta(\gamma,\tau)=\gamma\tau $. Let  $ v,w\in G_s $, and show that

 $$ d\eta(v,w)=d\eta\big((v,0)+(0,w)\big)=v+w. $$ 

12 Let $G$ be a connected Lie group, and let $\varphi: G \to H$ be a homomorphism with a discrete kernel. Prove that the kernel lies in the center of $G$. Use this fact to prove that the fundamental group of a Lie group is abelian.

13 Prove that Example 3.5(d) is, up to isomorphism, the only 2-dimensional non-abelian Lie algebra. Conclude that Example 3.3(h) is, up to isomorphism, the unique simply connected 2-dimensional non-abelian Lie group.

14 Show that there are matrices  $ A, B \in \mathrm{gl}(n, \mathbb{C}) $ such that  $ e^{A+B} \neq e^{A} e^{B} $.

15 Prove that the exponential map for $GI(n,\mathbb{C})$ is surjective. (Outline: First, by using the Jordan canonical form, reduce the problem to that of showing that each elementary Jordan matrix (a matrix with a fixed constant $\lambda$ on the diagonal, with $1$'s immediately above each diagonal entry, and with zeros elsewhere) in $GI(j,\mathbb{C})$, for $1 \leq j \leq n$, is the exponential of an element of $gl(j,\mathbb{C})$. Let $A$ be an elementary Jordan matrix. Write $A$ as $(\lambda I) \cdot N$ where the diagonal entries of $N$ are $1^s$. Prove that $\lambda I = e^{A_1}$ and that $N = e^{A_s}$, where $A_1 A_s = A_s A_1$. To find $A_s$, observe that since sufficiently high powers of the difference $I - N$ vanish, $N$ has a logarithm, namely,

 $$ \log N=-\sum_{k=1}^{\infty}\frac{(I-N)^{k}}{k}\;. $$ 

Use a formal power series argument to show that  $ e^{\log N} = N $.

16 Let $G$ be a Lie group. A vector field $Y$ on $G$ is right invariant if $Y$ is $r_\sigma$-related to itself for each $\sigma\in G$. Prove that the set of right invariant vector fields on $G$ forms a Lie algebra under the Lie bracket operation and is naturally isomorphic as a vector space with $G_\sigma$. Let $\varphi: G\to G$ be the diffeomorphism defined by $\varphi(\sigma)=\sigma^{-1}$. Prove that if $X$ is a left invariant vector field on $G$, then $d\varphi(X)$ is the right invariant vector field whose value at $e$ is $-\chi(e)$. Prove that $X\mapsto d\varphi(X)$ gives a Lie algebra isomorphism of the Lie algebra of left invariant vector fields on $G$ with the Lie algebra of right invariant vector fields on $G$.

17 Find an example of a Lie group $G$ with a Lie subgroup $A$ that is not closed in $G$.

18 Let $G$ be an $n$-dimensional abelian connected Lie group. Prove there is an integer $k$, $0 \leq k \leq n$, such that $G$ is isomorphic with $\mathbb{R}^{n-k} \times T^k$ where $T^k$ is a torus of dimension $k$. First, prove that up to isomorphism, $\mathbb{R}^n$ is the unique simply connected abelian Lie group. Next, show that if $D$ is a discrete subgroup of $\mathbb{R}^n$, then either $D = \{0\}$ or there is an integer $k$, $1 \leq k \leq n$, and $k$ linearly independent vectors $v_1, \ldots, v_k$ in $\mathbb{R}^n$ which generate $D$. To prove this, suppose that $D \neq \{0\}$, and let $k$ be the smallest integer such that $D$ is contained in a $k$-dimensional subspace $V$ of $\mathbb{R}^n$. Find a basis $w_1, \ldots, w_k$ for $V$ such that the $w_i \in D$. Let

 $$ A_{i}=\left\{\sum_{j=1}^{\epsilon}r_{j}w_{j}\colon0\leq r_{j}\leq1,r_{\epsilon}>0\right\} $$ 

for $i = 1, \ldots, k$. Choose $v_i$ to be an element of $A_i \cap D$ with smallest possible coefficient $r_i$. Then $\{v_1, \ldots, v_k\}$ will be a linearly independent set generating $D$.

19 Supply a proof for 3.56.

20 Prove that the group of automorphisms of a connected Lie group $G$ is itself a Lie group. (Outline: Let $\tilde{G}$ be the simply connected covering group of $G$, and let $\pi$ be the covering homomorphism. Let $D = \ker \pi$. We know from 3.57(b) that the group $A(\tilde{G})$ of automorphisms of $\tilde{G}$ is a Lie group. Show that the group of automorphisms of $G$ is naturally isomorphic with the (closed) subgroup of $A(\tilde{G})$ consisting of those automorphisms of $\tilde{G}$ which map $D$ onto $D$.)

21 Prove that  $ U(n) $ is diffeomorphic with  $ S^{1} \times SU(n) $.

22 (a) Deduce from a “super-triangularization” argument similar to that following 3.35(6), but now using unit eigenvectors and orthogonal complements, that if $A$ is a hermitian matrix (that is, $A$ is complex and $\bar{A}=A^{t}$), then there exists a unitary

matrix $B$ such that $BAB^{-1}$ is diagonal. By a similar argument, prove that if $A$ is a real symmetric matrix ($A = A^{t}$), then there exists a real orthogonal matrix $B$ such that $BAB^{-1}$ is diagonal.

(b) Using part (a) and 3.46(7), prove that the exponential map maps the hermitian matrices one-to-one onto the set of positive definite (all eigenvalues positive) hermitian matrices. Deduce also that the exponential map maps the real symmetric matrices one-to-one onto the set of positive definite symmetric matrices.

23 Use part (b) of Exercise 22 to prove that the polar decomposition 3.68(1) is unique. (Hint: If  $ \sigma = PR = P_{1}R_{1} $, first prove that  $ P^{2} = P_{1}^{2} $, then apply part (b) of Exercise 22 to P and  $ P_{1} $.)

24 Prove that every matrix  $ \sigma \in G l(n, \mathbb{C}) $ can uniquely be written as a product  $ \sigma = PR $, where  $ P $ is a positive definite hermitian matrix and  $ R $ is a unitary matrix.

25 Prove that $GI(n,\mathbb{C})$ is connected.

26 Complete the details of 3.65(b) and (c).
