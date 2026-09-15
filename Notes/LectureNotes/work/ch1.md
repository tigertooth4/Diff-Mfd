After establishing some notational conventions which will be used throughout the book, we will begin with the notion of a differentiable manifold. These are spaces which are locally like Euclidean space and which have enough structure so that the basic concepts of calculus can be carried over. In this first chapter we shall primarily be concerned with the analogs and implications for manifolds of the fundamental theorems of differential calculus. Later, in Chapter 4, we shall consider the theory of integration on manifolds.

From the notion of directional derivative in Euclidean space we will obtain the notion of a tangent vector to a differentiable manifold. We will study mappings between manifolds and the effect that mappings have on tangent vectors. We will investigate the implications for mappings of manifolds of the classical inverse and implicit function theorems. We will see that the fundamental existence and uniqueness theorems for ordinary differential equations translate into existence and uniqueness statements for integral curves of vector fields. The chapter closes with the Frobenius theorem, which pertains to the existence and uniqueness of integral manifolds of involutive distributions on manifolds.

##### PRELIMINARIES

1.1 Some Basic Notation and Terminology Throughout this text we will describe sets either by listings of their elements, for example

 $$ \{a_{1},\ldots,a_{n}\}, $$ 

or by expressions of the form

 $$ \{x\colon P\}, $$ 

which denote the set of all $x$ satisfying property $P$. The expression $a\in A$ means that $a$ is an element of the set $A$. If a set $A$ is a subset of a set $B$ (that is, $a\in B$ whenever $a\in A$), we write $A\subset B$. If $A\subset B$ and $B\subset A$, then $A$ equals $B$, denoted $A=B$. The negations of $\in$, $\subset$ and $=$ are denoted by $\notin$, $\notin$, and $\neq$ respectively. $A$ set $A$ is a proper subset of $B$ if $A\subset B$ but $A\neq B$.

We will denote the empty set by $\varnothing$. We will often denote a collection $\{U_a : \alpha \in A\}$ of sets $U_a$ indexed by the set $A$ simply by $\{U_a\}$ if explicit mention of the index set is not necessary. The union of the sets in the collection $\{U_a : \alpha \in A\}$ will be denoted $\bigcup_{a \in A} U_a$ or simply $\bigcup U_a$. Similarly, their intersection will be denoted $\bigcap_{a \in A} U_a$ or simply $\bigcap U_a$.

 $$ \bigcup_{\alpha\in A}U_{\alpha}=\{a\colon a{~b e l o n g s~t o~s o m e~}U_{\alpha}\}. $$ 

 $$ \bigcap_{a\in A}U_{a}=\{a\colon a{~b e l o n g s~t o~e v e r y~}U_{a}\}. $$ 

The expression $f\colon A\to B$ means that $f$ is a mapping of the set $A$ into the set $B$. When describing a mapping by describing its effect on individual elements, we use the special arrow $\mapsto$; thus “the mapping $m\mapsto f(m)$ of $A$ into $B$” means that $f$ is a mapping of the set $A$ into the set $B$ taking the element $m$ of $A$ into the element $f(m)$ of $B$. If $U\subset A$, then $f\mid U$ denotes the restriction of $f$ to $U$, and $f(U)=\{b\in B: f(a)=b$ for some $a\in U\}$. If $C\subset B$, then $f^{-1}(C)=\{a\in A: f(a)\in C\}$. A mapping $f$ is one-to-one (also denoted 1:1), or injective, if whenever $a$ and $b$ are distinct elements of $A$, then $f(a)\neq f(b)$. A mapping $f$ is onto, or surjective, if $f(A)=B$.

If $f\colon A \to B$ and $g\colon C \to D$, then the composition $g\circ f$ is the map

 $$ g\circ f\colon f^{-1}(B\cap C)\to D $$ 

defined by $g \circ f(a) = g(f(a))$ for every $a \in f^{-1}(B \cap C)$. For notational convenience, we shall not exclude the case in which $f^{-1}(B \cap C) = \varnothing$. That is, given any two mappings $f$ and $g$, we shall consider their composition $g \circ f$ as being defined, with the understanding that the domain of $g \circ f$ may well be the empty set.

The cartesian product  $ A \times B $ of two sets  $ A $ and  $ B $ is the set of all pairs  $ (a, b) $ of points  $ a \in A $ and  $ b \in B $. If  $ f: A \to C $ and  $ g: B \to D $, then the cartesian product  $ f \times g $ of the maps  $ f $ and  $ g $ is the map  $ (a, b) \mapsto (f(a), g(b)) $ of  $ A \times B $ into  $ C \times D $.

We shall denote the identity map on any set by “id.”

A diagram of maps such as

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//70c03fd3-9bd4-4d08-8396-413c3dc5c0ea/markdown_2/imgs/img_in_image_box_394_882_575_1063.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A11Z%2F-1%2F%2F46dbfc2b18f5dcaf548bd4d8ac856d9d5c58a9958180b31e3426fff2426aca28" alt="Image" width="19%" /></div>

is called commutative if  $ g \circ f = h $.

We shall always use the term function to mean a mapping into the real numbers.

Let  $ d \geq 1 $ be an integer, and let

 $  \mathbb{R}^d = \{a: a = (a_1, \ldots, a_d) \text{ where the } a_i \text{ are real numbers}\}  $.

Then $\mathbb{R}^d$ is the $d$-dimensional Euclidean space. In the case $d=1$, we denote the real line $\mathbb{R}^1$ simply by $\mathbb{R}$. The origin $(0,\ldots,0)$ in Euclidean space of any dimension will be denoted 0. The notations $[a,b]$ and $(a,b)$ denote as usual the intervals of the real line $a\leq t\leq b$ and $a<t<b$ respectively. The function $r_t:\mathbb{R}^d\to\mathbb{R}$ defined by

 $$ r_{i}(a)=a_{i}\;, $$ 

where  $ a = (a_1, \ldots, a_d) \in \mathbb{R}^d $, is called the  $ i $th (canonical) coordinate function on  $ \mathbb{R}^d $. The canonical coordinate function  $ r_1 $ on  $ \mathbb{R} $ will be denoted simply by  $ r $. Thus  $ r(a) = a $ for each  $ a \in \mathbb{R} $. If  $ f: X \to \mathbb{R}^d $, then we let

 $$ f_{t}=r_{t}\circ f, $$ 

where $f_{i}$ is called the $i$th component function of $f$.

If $f\colon \mathbb{R} \to \mathbb{R}$ and $t \in \mathbb{R}$, then we denote the derivative of $f$ at $t$ by

 $$ \begin{array}{r}{\frac{d}{d r}\bigg\vert_{t}(f)=\frac{d f}{d r}\bigg\vert_{t}=\operatorname*{l i m}_{h\to0}\frac{f(t+h)-f(t)}{h}.}\end{array} $$ 

If $f: \mathbb{R}^n \to \mathbb{R}$, if $1 \leq i \leq n$, and if $t = (t_1, \ldots, t_n) \in \mathbb{R}^n$, then we denote the partial derivative of $f$ with respect to $r_t$ at $t$ by

 $$ \frac{\partial}{\partial r_{\mathfrak{t}}}\Big\vert_{t}(f)=\frac{\partial f}{\partial r_{\mathfrak{t}}}\Big\vert_{t}=\operatorname*{l i m}_{\hbar\to0}\frac{f(t_{1},\ldots,t_{\mathfrak{t}-1},t_{\mathfrak{t}}+\hbar,t_{\mathfrak{t}+1},\ldots,t_{n})-f(t)}{\hbar}. $$ 

If $p \in \mathbb{R}^d$, then $B_p(r)$ will denote the open ball of radius $r$ about $p$. The open ball of radius $r$ about the origin will be denoted simply by $B(r)$. $C(r)$ will denote the open cube with sides of length $2r$ about the origin in $\mathbb{R}^d$. That is,

 $$ C(r)=\{(a_{1},\ldots,a_{d})\in\mathbb{R}^{d}\colon|a_{i}|<r\mathrm{f o r~a l l}i\}. $$ 

We shall use C to denote the complex number field and  $ C^{*} $ to denote complex n-space.

 $$ \mathbb{C}^{n}=\{(z_{1},\ldots,z_{n})\colon z_{i}\in\mathbb{C}\mathrm{~f o r~}1\leq i\leq n\}. $$ 

Unless we indicate otherwise, we shall always use the term neighborhood in the sense of open neighborhood. If $A$ is a subset of a topological space, its closure will be denoted by $\widetilde{A}$. If $\varphi$ is a function on a topological space $X$, the support of $\varphi$ is the subset of $X$ defined by

 $$ \mathrm{s u p p}\varphi=\overline{{\varphi^{-1}(\mathbb{R}-\{0\})}}. $$ 

We use the Kronecker index

 $$ \delta_{i j}=\left\{\begin{aligned}{}&{{}1,\quad}&{i=j}\\ {}&{{}0,\quad}&{i\neq j.}\\ \end{aligned}\right. $$ 

If  $ \alpha=(\alpha_{1},\ldots,\alpha_{d}) $ is a d-tuple of non-negative integers, then we set

 $$ [\alpha]=\textstyle\sum\alpha_{i}, $$ 

 $$ \alpha_{1}=\alpha_{1}\alpha_{2}\cdots\alpha_{d}, $$ 

and

 $$ \frac{\partial^{\alpha}}{\partial r^{\alpha}}=\frac{\partial^{[\alpha]}}{\partial r_{1}^{\alpha_{1}}\cdots\partial r_{d}^{\alpha_{d}}}. $$ 

If  $ \alpha = (0, \ldots, 0) $, then we let

 $$ \frac{\partial^{a}}{\partial r^{a}}(f)=f. $$ 

##### DIFFERENTIABLE MANIFOLDS

1.2 Definitions Let $U \subset \mathbb{R}^d$ be open, and let $f: U \to \mathbb{R}$. We say that $f$ is differentiable of class $C^k$ on $U$ (or simply that $f$ is $C^k$), for $k$ a non-negative integer, if the partial derivatives $\partial^n f / \partial r^n$ exist and are continuous on $U$ for $|\alpha| \leq k$. In particular, $f$ is $C^0$ if $f$ is continuous. If $f: U \to \mathbb{R}^n$, then $f$ is differentiable of class $C^k$ if each of the component functions $f_i = r_i \circ f$ is $C^k$. We say that $f$ is $C^\infty$ if it is $C^k$ for all $k \geq 0$.

1.3 Definitions A locally Euclidean space M of dimension d is a Hausdorff topological space M for which each point has a neighborhood homeomorphic to an open subset of Euclidean space  $ R^{\ell} $. If  $ \varphi $ is a homeomorphism of a connected open set  $ U \subset M $ onto an open subset of  $ R^{\ell} $,  $ \varphi $ is called a coordinate map, the functions  $ x_t = r_t \circ \varphi $ are called the coordinate functions, and the pair  $ (U, \varphi) $ (sometimes denoted by  $ (U, x_1, \ldots, x_d) $) is called a coordinate system. A coordinate system  $ (U, \varphi) $ is called a cubic coordinate system if  $ \varphi(U) $ is an open cube about the origin in  $ R^{\ell} $. If  $ m \in U $ and  $ \varphi(m) = 0 $, then the coordinate system is said to be centered at m.

1.4 Definitions A differentiable structure  $ \mathcal{F} $ of class  $ C^k $ ( $ 1 \leq k \leq \infty $) on a locally Euclidean space  $ M $ is a collection of coordinate systems  $ \{(U_a, \varphi_a): a \in A\} $ satisfying the following three properties:

(a)  $ \bigcup_{a\in A} U_a = M $.

(b)  $ \varphi_{\alpha} \circ \varphi_{\beta}^{-1} $ is  $ C^{k} $ for all  $ \alpha, \beta \in A $.

(c) The collection $\mathcal{F}$ is maximal with respect to (b); that is, if $(U,\varphi)$ is a coordinate system such that $\varphi\circ\varphi_{x}^{-1}$ and $\varphi_{x}\circ\varphi^{-1}$ are $C^{k}$ for all $\alpha\in A$, then $(U,\varphi)\in\mathcal{F}$.

If  $ \mathcal{F}_{0}=\{(U_{a},\varphi_{a})\colon a\in A\} $ is any collection of coordinate systems satisfying properties (a) and (b), then there is a unique differentiable structure  $ \mathcal{F} $ containing  $ \mathcal{F}_{0} $. Namely, let

 $$ \mathcal{F}=\{(U,\varphi)\colon\varphi\circ\varphi_{a}^{-1}\mathrm{~a n d~}\varphi_{a}\circ\varphi^{-1}\stackrel{\circ}{{\mathbf{a r e}}}C^{k}\mathrm{~f o r~a l l~}\varphi_{a}\in\mathcal{F}_{0}\}. $$ 

Then $\mathcal{F}$ contains $\mathcal{F}_{0}$, clearly satisfies (a), and it is easily checked that $\mathcal{F}$ satisfies (b). Now $\mathcal{F}$ is maximal by construction, and so $\mathcal{F}$ is a differentiable structure containing $\mathcal{F}_{0}$. Clearly $\mathcal{F}$ is the unique such structure.

We mention two other fundamental types of differentiable structures on locally Euclidean spaces, types that we shall not treat in this text, namely, the structure of class  $ C^{\infty} $ and the complex analytic structure. For a differentiable structure of class  $ C^{\infty} $, one requires that the compositions in (b) are locally given by convergent power series. For a complex analytic structure on a 2d-dimensional locally Euclidean space, one requires that the coordinate systems have range in complex d-space  $ C^{d} $ and overlap holomorphically.

$\hat{A}$ d-dimensional differentiable manifold of class $C^{k}$ (similarly $C^{k}$ or complex analytic) is a pair $(M,\mathcal{F})$ consisting of a $d$-dimensional, second countable, locally Euclidean space $M$ together with a differentiable structure $\mathcal{F}$ of class $C^{k}$. We shall usually denote the differentiable manifold $(M,\mathcal{F})$ simply by $M$, with the understanding that when we speak of the “differentiable manifold $M$” we are considering the locally Euclidean space $M$ with some given differentiable structure $\mathcal{F}$. Our attention will be restricted solely to the case of class $C^{k}$, so by differentiable we will always mean differentiable of class $C^{k}$. We also use the terminology smooth to indicate differentiability of class $C^{k}$. We often refer to differentiable manifolds simply as manifolds, with differentiability of class $C^{k}$ always implicitly assumed. A manifold can be viewed as a triple consisting of an underlying point set, a second countable locally Euclidean topology for this set, and a differentiable structure. If $X$ is a set, by a manifold structure on $X$ we shall mean a choice of both a second countable locally Euclidean topology for $X$ and a differentiable structure.

Even though we shall restrict our attention to the $C^\infty$ case, many of our theorems do, however, have $C^k$ versions for $k < \infty$, which are essentially no more complicated than the ones we shall obtain. They simply require that one keep track of degrees of differentiability, for differentiating a $C^k$ function may only yield a function of class $C^{k-1}$ if $1 \leq k < \infty$.

Unless we indicate otherwise, we shall always use M and N to denote differentiable manifolds, and  $ M^{d} $ will indicate that M is a manifold of dimension d.

### 1.5 Examples

(a) The standard differentiable structure on Euclidean space $\mathbb{R}^d$ is obtained by taking $\mathcal{F}$ to be the maximal collection (with respect to $1.4(b)$) containing $(\mathbb{R}^d, i)$, where $i: \mathbb{R}^d \to \mathbb{R}^d$ is the identity map.

(b) Let $V$ be a finite dimensional real vector space. Then $V$ has a natural manifold structure. Indeed, if $\{e_i\}$ is a basis of $V$, then the elements of the dual basis $\{r_i\}$ are the coordinate functions of a global coordinate system on $V$. Such a global coordinate system uniquely determines a differentiable structure $\mathcal{F}$ on $V$. This differentiable structure is independent of the choice of basis, since different bases give $C^\infty$ overlapping coordinate systems. In fact, the change of coordinates is given simply by a constant non-singular matrix.

(c) Complex $n$-space $\mathbb{C}^{n}$ is a real $2n$-dimensional vector space, and so, by Example (b), has a natural structure as a $2n$-dimensional real manifold. If $\{e_{i}\}$ is the canonical complex basis in which $e_{i}$ is the $n$-tuple consisting of zeros except for a $1$ in the $i$th spot, then

 $$ \{e_{1},\ldots,e_{n},\sqrt{-1}e_{1},\ldots,\sqrt{-1}e_{n}\} $$ 

is a real basis for $C^{n}$, and its dual basis is the canonical global coordinate system on $C^{n}$.

(d) The d-sphere is the set

 $$ S^{d}=\{a\in\mathbb{R}^{d+1}\colon\sum_{i=1}^{d+1}a_{i}^{\sharp}=1\}. $$ 

Let $n = (0, \ldots, 0, 1)$ and $s = (0, \ldots, 0, -1)$. Then the standard differentiable structure on $S^d$ is obtained by taking $\mathcal{F}$ to be the maximal collection containing $(S^d - n, p_n)$ and $(S^d - s, p_s)$, where $p_n$ and $p_s$ are stereographic projections from $n$ and $s$ respectively.

(e) An open subset $U$ of a differentiable manifold $(M,\mathcal{F}_{M})$ is itself a differentiable manifold with differentiable structure

 $$ \mathcal{F}_{U}=\{(U_{\alpha}\cap U,\varphi_{\alpha}\big|U_{\alpha}\cap U)\colon(U_{\alpha},\varphi_{\alpha})\in\mathcal{F}_{M}\}. $$ 

Unless specified otherwise, open subsets of differentiable manifolds will always be given this natural differentiable structure.

(f) The general linear group $Gl(n,\mathbb{R})$ is the set of all $n\times n$ non-singular real matrices. If we identify in the obvious way the points of $\mathbb{R}^{n^{3}}$ with $n\times n$ real matrices, then the determinant becomes a continuous function on $\mathbb{R}^{n^{3}}$. $Gl(n,\mathbb{R})$ receives a manifold structure as the open subset of $\mathbb{R}^{n^{3}}$ where the determinant function does not vanish.

(g) Product manifolds. Let $(M_{1},\mathcal{F}_{1})$ and $(M_{2},\mathcal{F}_{2})$ be differentiable manifolds of dimensions $d_{1}$ and $d_{2}$ respectively. Then $M_{1}\times M_{2}$ becomes a differentiable manifold of dimension $d_{1}+d_{2}$, with differentiable structure $\mathcal{F}$ the maximal collection containing

 $$ \{U_{\alpha}\times V_{\beta},\varphi_{\alpha}\times\psi_{\beta}\colon U_{\alpha}\times V_{\beta}\to $$ 

 $$ \mathbb{R}^{d_{1}}\times\mathbb{R}^{d_{2}})\colon(U_{\alpha},\varphi_{\alpha})\in\mathcal{F}_{1},(V_{\beta},\psi_{\beta})\in\mathcal{F}_{2}\}. $$ 

1.6 Definitions Let $U \subset M$ be open. We say that $f: U \to \mathbb{R}$ is a $C^\infty$ function on $U$ (denoted $f \in C^\infty(U)$) if $f \circ \varphi^{-1}$ is $C^\infty$ for each coordinate map $\varphi$ on $M$. A continuous map $\psi: M \to N$ is said to be differentiable of class $C^\infty$ (denoted $\psi \in C^\infty(M,N)$ or simply $\psi \in C^\infty$) if $g \circ \psi$ is a $C^\infty$ function on $\psi^{-1}$ (domain of $g$) for all $C^\infty$ functions $g$ defined on open sets in $N$. Equivalently, the continuous map $\psi$ is $C^\infty$ if and only if $\varphi \circ \psi \circ \tau^{-1}$ is $C^\infty$ for each coordinate map $\tau$ on $M$ and $\omega$ on $N$.

Clearly the composition of two differentiable maps is again differentiable. Observe that a mapping $\psi: M \to N$ is $C^\infty$ if and only if for each $m \in M$ there exists an open neighborhood $U$ of $m$ such that $\psi \mid U$ is $C^\infty$.

##### THE SECOND AXIOM OF COUNTABILITY

The second axiom of countability has many consequences for manifolds. Among them, manifolds are normal, metrizable, and paracompact. Paracompactness implies the existence of partitions of unity, an extremely useful tool for piecing together global functions and structures out of local ones, and conversely for representing global structures as locally finite sums of local ones. After giving the necessary definitions, we shall give a simple direct proof of paracompactness for manifolds, and shall then derive the existence of partitions of unity. It is evident that manifolds are regular topological spaces and their normality follows easily from this and the paracompactness. We shall leave the proof that manifolds are normal as an exercise. For the fact that manifolds are metrizable, see [13].

1.7 Definitions A collection $\{U_e\}$ of subsets of $M$ is a cover of a set $W \subset M$ if $W \subset \bigcup U_e$. It is an open cover if each $U_e$ is open. A subcollection of the $U_e$ which still covers is called a subcover. A refinement $\{V_\beta\}$ of the cover $\{U_e\}$ is a cover such that for each $\beta$ there is an $\alpha$ such that $V_\beta \subset U_e$. A collection $\{A_e\}$ of subsets of $M$ is locally finite if whenever $m \in M$ there exists a neighborhood $W_m$ of $m$ such that $W_m \cap A_e \neq \varnothing$ for only finitely many $\alpha$. A topological space is paracompact if every open cover has an open locally finite refinement.

1.8 Definition A partition of unity on $M$ is a collection $\{\varphi_i: i \in I\}$ of $C^\infty$ functions on $M$ such that

(a) The collection of supports {supp $\varphi_{i}$: $i \in I\}$ is locally finite.

(b)  $ \sum_{i\in I}\varphi_i(p)=1 $ for all  $ p\in M $, and  $ \varphi_i(p)\geq0 $ for all  $ p\in M $ and  $ i\in I $.

A partition of unity $\{\varphi_i: i \in I\}$ is subordinate to the cover $\{U_e: \alpha \in A\}$ if for each $i$ there exists an $\alpha$ such that $\text{supp} \varphi_i \subset U_e$. We say that it is subordinate to the cover $\{U_i: i \in I\}$ with the same index set as the partition of unity if $\text{supp} \varphi_i \subset U_i$ for each $i \in I$.

1.9 Lemma Let X be a topological space which is locally compact (each point has at least one compact neighborhood), Hausdorff, and second countable (manifolds, for example). Then X is paracompact. In fact, each open cover has a countable, locally finite refinement consisting of open sets with compact closures.

PROOF We prove first that there exists a sequence  $ \{G_{i}: i = 1, 2, \ldots\} $ of open sets such that

 $$ \begin{aligned}{\overline{{G_{i}}}}&{{}{~i s~c o m p a c t,}}\\ {\overline{{G_{i}}}}&{{}\subset G_{i+1},}\\ {X}&{{}=\bigcup_{i=1}^{\infty}G_{i}.}\\ \end{aligned} $$ 

Let $\{U_{i}: i=1,2,\ldots\}$ be a countable basis of the topology of $X$ consisting of open sets with compact closures. Such a basis can be obtained by starting with any countable basis and selecting the subcollection consisting of basic sets with compact closures. The fact that $X$ is Hausdorff and locally compact implies that this subcollection is itself a basis. Now, let $G_{1}=U_{1}$. Suppose that

 $$ G_{k}=U_{1}\cup\cdots\cup U_{j_{k}}. $$ 

Then let  $ j_{k+1} $ be the smallest positive integer greater than  $ j_{k} $ such that

 $$ \overline{{G}}_{k}\subset\bigcup_{i=1}^{j_{k+1}}U_{i}, $$ 

 $$ G_{k+1}=\bigcup_{i=1}^{j_{k+1}}U_{i}. $$ 

and define

This defines inductively a sequence  $ \{G_{k}\} $ satisfying (1).

 $$ \bigcirc_{G_{1}\atop G_{i}}\quad\cdots\quad\bigcirc_{G_{i-1}\atop G_{i-1}}\quad\vdots\quad\bigcirc_{G_{i-1}\atop G_{i}}\quad\vdots\quad\bigcirc_{G_{i+1}\atop G_{i+1}} $$ 

Let $\{U_n : \alpha \in A\}$ be an arbitrary open cover. The set $\overline{G_i} - G_{i-1}$ is compact and contained in the open set $G_{i+1} - \overline{G_{i-1}}$. For each $i \geq 3$ choose a finite subcover of the open cover $\{U_n \cap (G_{i+1} - \overline{G_{i-1}}): \alpha \in A\}$ of $\overline{G_i} - G_{i-1}$, and choose a finite subcover of the open cover $\{U_n \cap G_i : \alpha \in A\}$ of the compact set $\overline{G_i}$. This collection of open sets is easily seen to be a countable, locally finite refinement of the open cover $\{U_n\}$, and consists of open sets with compact closures.

1.10 Lemma There exists a non-negative $C^{\infty}$ function $\varphi$ on $\mathbb{R}^{d}$ which equals 1 on the closed cube $\overline{C(1)}$ and zero on the complement of the open cube $C(2)$.

PROOF We need only let $\varphi$ be the product

 $$ \varphi=(h\circ r_{1})\cdot\cdot\cdot(h\circ r_{d}), $$ 

where $h$ is a non-negative $C^{\infty}$ function on the real line which is 1 on $[-1,1]$ and zero outside of $(-2,2)$. To construct such an $h$, we start with the function

 $$ f(t)=\left\{\begin{aligned}{}&{{}e^{-1/t}}&{}&{{}t>0}\\ {}&{{}0}&{}&{{}t\leq0}\\ \end{aligned}\right. $$ 

which is non-negative, $C^{\infty}$, and positive for $t>0$. Then the function

 $$ g(t)=\frac{f(t)}{f(t)+f(1-t)} $$ 

is non-negative, $C^\infty$, and takes the value 1 for $t \geq 1$ and the value zero for $t \leq 0$. We obtain the desired function $h$ by setting

 $$ h(t)=g(t+2)g(2-t). $$ 

1.11 Theorem (Existence of Partitions of Unity) Let $M$ be a differentiable manifold and $\{U_a: a \in A\}$ an open cover of $M$. Then there exists a countable partition of unity $\{\varphi_i: i = 1, 2, 3, \ldots\}$ subordinate to the cover $\{U_a\}$ with $\operatorname{supp} \varphi_i$ compact for each $i$. If one does not require compact supports, then there is a partition of unity $\{\varphi_a\}$ subordinate to the cover $\{U_a\}$ (that is, $\operatorname{supp} \varphi_a \subset U_a$) with at most countably many of the $\varphi_a$ not identically zero.

PROOF Let the sequence $\{G_i\}$ cover $M$ as in 1.9(1), and set $G_0 = \varnothing$. For $p \in M$, let $i_p$ be the largest integer such that $p \in M - \overline{G_{i_p}}$. Choose an $\alpha_p$ such that $p \in U_{\alpha_p}$, and let $(V, \tau)$ be a coordinate system centered at $p$ such that $V \subset U_{\alpha_p} \cap (G_{i_p+2} - \overline{G_{i_p}})$ and such that $\tau(V)$ contains the closed cube $\overline{C(2)}$. Define

 $$ \psi_{o}=\left\{\begin{aligned}{}&{{}\varphi^{\circ}\tau}&{\quad\mathrm{o n~}V}\\ {}&{{}0}&{\quad\mathrm{e l s e w h e r e}}\\ \end{aligned}\right. $$ 

where $\varphi$ is the function $1.10(1)$. Then $\psi_s$ is a $C^\infty$ function on $M$ which has the value 1 on some open neighborhood $W_s$ of $p$, and has compact support lying in $V \subset U_{s_p} \cap (G_{t_p+1} - \overline{G}_{t_p})$. For each $i \geq 1$, choose a finite set of points $p$ in $M$ whose corresponding $W_s$ neighborhoods cover $\overline{G}_t - G_{t-1}$. Order the corresponding $\psi_s$ functions in a sequence $\psi_j, j=1,2,3,\ldots$. The supports of the $\psi_j$ form a locally finite family of subsets of $M$. Thus the function

 $$ \psi=\sum_{j=1}^{\infty}\psi_{j} $$ 

is a well-defined $C^{\infty}$ function on $M$, and moreover $\psi(p) > 0$ for each $p \in M$. For each $i = 1, 2, 3, \ldots$ define

 $$ \varphi_{i}=\frac{\psi_{i}}{\psi_{-}}. $$ 

Then the functions $\{\varphi_i: i=1,2,3,\ldots\}$ form a partition of unity subordinate to the cover $\{U_a\}$ with $\operatorname{supp} \varphi_i$ compact for each $i$. If we let $\varphi_a$ be identically zero if no $\varphi_i$ has support in $U_a$, and otherwise let $\varphi_a$ be the sum of the $\varphi_i$ with support in $U_a$, then $\{\varphi_a\}$ is a partition of unity subordinate to the cover $\{U_a\}$ with at most countably many of the $\varphi_a$ not identically zero. To see that the support of $\varphi_a$ lies in $U_a$, observe that if $\mathcal{A}$ is a locally finite family of closed sets, then $\overline{\mathbf{U}A} = \bigcup_{A\in\mathcal{A}} A$.

Observe, however, that the support of $\varphi_{a}$ is not necessarily compact.

Corollary Let $G$ be open in $M$, and let $A$ be closed in $M$, with $A \subset G$. Then there exists a $C^{\infty}$ function $\varphi: M \to \mathbb{R}$ such that

(a)  $ 0 \leq \varphi(p) \leq 1 $ for all  $ p \in M $.

(b)  $ \varphi(p) = 1 $ if  $ p \in A $.

(c) supp  $ \varphi \subset G $.

PROOF There is a partition of unity $\{\varphi, \psi\}$ subordinate to the cover $\{G, M - A\}$ of $M$ with $\operatorname{supp} \varphi \subset G$ and $\operatorname{supp} \psi \subset M - A$. Then $\varphi$ is the desired function.

#### TANGENT VECTORS AND DIFFERENTIALS

1.12 A vector $v$ with components $v_{1}, \ldots, v_{d}$ at a point $p$ in Euclidean space $\mathbb{R}^{d}$ can be thought of as an operator on differentiable functions. Specifically, if $f$ is differentiable on a neighborhood of $p$, then $v$ assigns to $f$ the real number $v(f)$ which is the directional derivative of $f$ in the direction $v$ at $p$. That is,

 $$ v(f)=v_{1}\frac{\partial f}{\partial r_{1}}\bigg|_{p}+\cdots+v_{d}\frac{\partial f}{\partial r_{d}}\bigg|_{p}. $$ 

This operation of the vector v on differentiable functions satisfies two important properties.

 $$ \begin{aligned}{v(f+\lambda g)}&{{}=v(f)+\lambda v(g);}\\ {v(f\cdot g)}&{{}=f(p)v(g)+g(p)v(f),}\\ \end{aligned} $$ 

whenever $f$ and $g$ are differentiable near $p$, and $\lambda$ is a real number. The first property says that $v$ acts linearly on functions, and the second says that $v$ is a derivation. This motivates our definition of tangent vectors on manifolds. They will be directional derivatives, that is, linear derivations on functions. The operation of taking derivatives depends only on local properties of functions, properties in arbitrarily small neighborhoods of the point at which the derivative is being taken. In order to express most conveniently this dependence of the derivative on the local nature of functions, we introduce the notion of germs of functions.

1.13 Definitions Let $m \in M$. Functions $f$ and $g$ defined on open sets containing $m$ are said to have the same germ at $m$ if they agree on some neighborhood of $m$. This introduces an equivalence relation on the $C^\infty$ functions defined on neighborhoods of $m$, two functions being equivalent if and only if they have the same germ. The equivalence classes are called $germs$, and we denote the set of germs at $m$ by $F_m$. If $f$ is a $C^\infty$ function on a neighborhood of $m$, then $f$ will denote its germ. The operations of addition, scalar multiplication, and multiplication of functions induce on $F_m$ the structure of an algebra over $\mathbb{R}$. A germ $f$ has a well-defined value $f(m)$ at $m$, namely, the value at $m$ of any representative of the germ. Let $F_m \subset F_m$ be the set of germs which vanish at $m$. Then $F_m$ is an ideal in $F_m$, and we let $F_m^k$ denote its $k$th power. $F_m^k$ is the ideal of $F_m$ consisting of all finite linear combinations of $k$-fold products of elements of $F_m$. These form a descending sequence of ideals $F_m \supset F_m \supset F_m^k \supset F_m^k \supset \cdots$.

1.14 Definition A tangent vector  $ v $ at the point  $ m \in M $ is a linear derivation of the algebra  $ \widetilde{F}_m $. That is, for all  $ \mathbf{f} $,  $ \mathbf{g} \in \widetilde{F}_m $ and  $ \lambda \in \mathbb{R} $,

 $$ \begin{array}{r l}{\mathrm{(a)}}&{v(\mathbf{f}+\lambda\mathbf{g})=v(\mathbf{f})+\lambda v(\mathbf{g}).}\end{array} $$ 

 $$ v(\mathbf{f}\cdot\mathbf{g})=\mathbf{f}(m)v(\mathbf{g})+\mathbf{g}(m)v(\mathbf{f}). $$ 

 $ M_m $ denotes the set of tangent vectors to  $ M $ at  $ m $ and is called the tangent space to  $ M $ at  $ m $. Observe that if we define  $ (v + w)(f) $ and  $ (\lambda v)(f) $ by

 $$ \begin{aligned}(v+w)(\mathbf{f})&=v(\mathbf{f})+w(\mathbf{f})\ $ \lambda v)(\mathbf{f})&=\lambda(v(\mathbf{f}))\end{aligned} $$ 

whenever $v, w \in M_m$ and $\lambda \in \mathbb{R}$, then $v + w$ and $\lambda v$ again are tangent vectors at $m$. So in this way $M_m$ becomes a real vector space. The fundamental property of the vector space $M_m$, which we shall establish in 1.17, is that its dimension equals the dimension of $M$. This definition of tangent vector

is not suitable in the $C^{k}$ case for $1 \leq k < \infty$. (We will discuss the $C^{k}$ case further in 1.21.) We give this definition of tangent vector for several reasons. One reason is that it is intrinsic; that is, it does not depend on coordinate systems. Another reason is that it generalizes naturally to higher order tangent vectors, as we shall see in 1.26.

1.15 If $c$ is the germ of a function with the constant value $c$ on a neighborhood of $m$, and if $v$ is a tangent vector at $m$, then $v(c) = 0$, for

 $$ v(\mathbf{c})=c v(\mathbf{1}), $$ 

and

1.16 Lemma  $ M_{m} $ is naturally isomorphic with  $ (F_{m}/F_{m}^{2})^{*} $. (The symbol  $ {}^{*} $ denotes dual vector space.)

 $$ v(\mathbf{1})=v(\mathbf{1}\cdot\mathbf{1})=1v(\mathbf{1})+1v(\mathbf{1})=2v(\mathbf{1}). $$ 

PROOF If $v \in M_m$, then $v$ is a linear function on $F_m$ vanishing on $F_m^2$ because of the derivation property. Conversely, if $\ell \in (F_m/F_m^2)^*$, we define a tangent vector $v_\ell$ at $m$ by setting $v_\ell(\mathbf{f}) = \ell(\{\mathbf{f} - \mathbf{f}(\mathbf{m})\})$ for $\mathbf{f} \in \widetilde{F}_m$. (Here $\mathbf{f}(\mathbf{m})$ denotes the germ of the function with the constant value $\mathbf{f}(m)$, and-) is used to denote cosets in $F_m/F_m^2$.) Linearity of $v_\ell$ on $\widetilde{F}_m$ is clear. It is a derivation since

 $$ \begin{aligned}{v_{\ell}(\mathbf{f}\cdot\mathbf{g})}&{{}=\ell\big(\{\mathbf{f}\cdot\mathbf{g}-\mathbf{f}(\mathbf{m})\mathbf{g}(\mathbf{m})\}\big)}\\ {}&{{}=\ell\big(\{(\mathbf{f}-\mathbf{f}(\mathbf{m}))(\mathbf{g}-\mathbf{g}(\mathbf{m}))+\mathbf{f}(\mathbf{m})\big(\mathbf{g}-\mathbf{g}(\mathbf{m})\big)}\\ {}&{{}\quad+\big(\mathbf{f}-\mathbf{f}(\mathbf{m})\big)\mathbf{g}(\mathbf{m})\}\big)}\\ {}&{{}=\ell\big(\{(\mathbf{f}-\mathbf{f}(\mathbf{m}))(\mathbf{g}-\mathbf{g}(\mathbf{m}))\}\big)+\mathbf{f}(m)\ell\big(\{\mathbf{g}-\mathbf{g}(\mathbf{m})\}\big)}\\ {}&{{}\quad+\mathbf{g}(m)\ell\big(\{\mathbf{f}-\mathbf{f}(\mathbf{m})\}\big)}\\ {}&{{}=\mathbf{f}(m)v_{\ell}(\mathbf{g})+\mathbf{g}(m)v_{\ell}(\mathbf{f}).}\\ \end{aligned} $$ 

Thus we obtain mappings of $M_{m}$ into $(F_{m}/F_{m}^{2})^{*}$, and vice versa. It is easily checked that these are inverses of each other and thus are iso morphisms.

### 1.17 Theorem  $ \dim\left(F_{m}/F_{m}^{2}\right)=\dim M. $

The proof is based on the following calculus lemma [31].

Lemma If $g$ is of class $C^k$ ($k \geq 2$) on a convex open set $U$ about $p$ in $\mathbb{R}^d$, then for each $q \in U$,

 $$ \begin{aligned}{\mathbf{g}(q)}&{{}=\mathbf{g}(p)+\sum_{i=1}^{d}\frac{\partial g}{\partial r_{i}}\bigg|_{p}\big(r_{i}(q)-r_{i}(p)\big)\quad.}\\ {}&{{}\quad+\sum_{i,j}\big(r_{i}(q)-r_{i}(p)\big)\big(r_{j}(q)-r_{j}(p)\big)\int_{0}^{1}(1-t)\frac{\partial^{2}g}{\partial r_{i}\partial r_{j}}\bigg|_{(p+t(q-p))}d t.}\\ \end{aligned} $$ 

In particular, if $g \in C^{\infty}$, then the second summation in (1) determines an element of $F_{p}^{2}$ since the integral as a function of $q$ is of class $C^{\infty}$.

PROOF OF 1.17 Let $(U,\varphi)$ be a coordinate system about $m$ with coordinate functions $x_1,\ldots,x_d$ ($d=\dim M$). Let $f\in F_m$. Apply (1) to $f\circ\varphi^{-1}$, and compose with $\varphi$ to obtain

 $$ f=\sum_{i=1}^{d}\frac{\partial(f\circ\varphi^{-1})}{\partial r_{i}}\bigg|_{\varphi(m)}(x_{i}-x_{i}(m))+\sum_{i,j}(x_{i}-x_{i}(m))(x_{j}-x_{j}(m)) $$ 

on a neighborhood of $m$, where $h \in C^{\infty}$. Thus

 $$ \mathbf{f}=\sum_{i=1}^{d}\frac{\partial(f\circ\varphi^{-1})}{\partial r_{i}}\bigg|_{\varphi(m)}\left(\mathbf{x}_{i}-\mathbf{x}_{i}(\mathbf{m})\right)\bmod F_{m}{}^{3}. $$ 

Hence $\{\{\mathbf{x}_{i}-\mathbf{x}_{i}(\mathbf{m})\}: i=1,\ldots,d\}$ spans $F_{m}/F_{m}^{2}$. Consequently $\dim F_{m}/F_{m}^{2}\leq d$. We claim that these elements are linearly independent. For suppose that

 $$ \sum_{i=1}^{d}a_{i}(\mathbf{x}_{i}-\mathbf{x}_{i}(\mathbf{m}))\in F_{\mathrm{m}}^{\mathrm{s}}. $$ 

Now,

 $$ \sum_{i=1}^{d}a_{i}\big(x_{i}-x_{i}(m)\big)\circ\varphi^{-1}=\sum_{i=1}^{d}a_{i}\big(r_{i}-r_{i}\big(\varphi(m)\big)\big). $$ 

Thus

 $$ \sum_{i=1}^{d}a_{i}\big(\mathbf{r}_{i}-\mathbf{r}_{i}\big(\mathbf{\varphi}(\mathbf{m})\big)\big)\in F_{\varphi(\mathbf{m})}^{2}\;. $$ 

But this implies that

 $$ \frac{\partial}{\partial r_{j}}\bigg|_{\substack{\varphi(m)}}\big(\textstyle\sum a_{i}\big(r_{i}-r_{i}\big(\varphi(m)\big)\big)\big)=0 $$ 

for $j=1,\ldots,d$, which implies that the $a_{i}$ must all be zero.

Corollary dim  $ M_{m} = \dim M $.

1.18 In practice we will treat tangent vectors as operating on functions rather than on their germs. If $f$ is a differentiable function defined on a neighborhood of $m$, and $v \in M_{m}$, we define

 $$ v(f)=v(\mathbf{f}). $$ 

Thus  $ v(f) = v(g) $ whenever f and g agree on a neighborhood of m, and clearly

 $$ \begin{aligned}{v(f+\lambda g)}&{{}=v(f)+\lambda v(g)\qquad(\lambda\in\mathbb{R}),}\\ {v(f\cdot g)}&{{}=f(m)v(g)+g(m)v(f),}\\ \end{aligned} $$ 

where  $ f + \lambda g $ and  $ f \cdot g $ are defined on the intersection of the domains of definition of f and g.

1.19 Definition Let $(U,\varphi)$ be a coordinate system with coordinate functions $x_{1},\ldots,x_{d}$, and let $m\in U$. For each $i\in(1,\ldots,d)$, we define

a tangent vector  $ (\partial/\partial x_i)|_{m} \in M_m $ by setting

 $$ \left(\frac{\partial}{\partial x_{i}}\bigg\vert_{m}\right)(f)=\frac{\partial(f\circ\varphi^{-1})}{\partial r_{i}}\bigg\vert_{\varphi(m)} $$ 

for each function $f$ which is $C^{\infty}$ on a neighborhood of $m$. We interpret (1) as the directional derivative of $f$ at $m$ in the $x_{i}$ coordinate direction. We also use the notation

 $$ \left.\frac{\partial f}{\partial x_{i}}\right|_{m}=\left(\left.\frac{\partial}{\partial x_{i}}\right|_{m}\right)(f). $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//61098b9b-10c0-4344-90c8-5e3f1bbc25cf/markdown_2/imgs/img_in_image_box_142_360_796_574.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A11Z%2F-1%2F%2F9024c648ef5b6611bdef4261ff784ff6d9056566eceed51c4c756d4dbc403aaa" alt="Image" width="68%" /></div>

### 1.20 Remarks on 1.19

(a) Clearly  $  ((\partial/\partial x_i)_m)(f)  $ depends only on the germ of  $  f  $ at  $  m  $, and (a) and (b) of 1.14 are satisfied; so  $  (\partial/\partial x_i)_m  $ is a tangent vector at  $  m  $. Moreover,  $  \{(\partial/\partial x_i)_m : i = 1, \ldots, d\}  $ is a basis of  $  M_m  $. Indeed, it is the basis of  $  M_m  $ dual to the basis  $  \{(\mathbf{x}_i - \mathbf{x}_1(\mathbf{m})) : i = 1, \ldots, d\}  $ of  $  F_m/F_m^2  $ since

 $$ \frac{\partial}{\partial x_{i}}\bigg|_{m}(x_{j}-x_{j}(m))=\delta_{ij}. $$ 

(b) If  $ v \in M_{m} $, then

 $$ v=\sum_{i=1}^{d}v(x_{i})\left.\frac{\partial}{\partial x_{i}}\right|_{\infty}. $$ 

Simply check that both sides give the same results when applied to the functions $(x_{j}-x_{j}(m))$.

(c) Suppose that $(U,\varphi)$ and $(V,\psi)$ are coordinate systems about $m$, with coordinate functions $x_{1},\ldots,x_{d}$ and $y_{1},\ldots,y_{d}$ respectively. Then it follows from remark (b) that

 $$ \frac{\partial}{\partial y_{j}}\Big|_{m}=\sum_{i=1}^{d}\frac{\partial x_{i}}{\partial y_{j}}\Big|_{m}\frac{\partial}{\partial x_{i}}\Big|_{m}. $$ 

Observe that $(\partial/\partial x_{i})$ depends on $\varphi$ and not only on $x_{i}$. In particular, if $x_{1}$ were equal to $y_{1}$, it would not necessarily follow that $\partial/\partial x_{1}$ equals $\partial/\partial y_{1}$.

(d) If we apply Definition 1.19 to the canonical coordinate system  $ r_{1}, \ldots, r_{d} $ on  $ R^{d} $, then the tangent vectors which we obtain are none other than the ordinary partial derivative operators  $ (\partial/\partial r_{i}) $.

1.21 Our proof of the finite dimensionality of  $ F_m/F_m^3 $ certainly fails in the  $ C^k $ case for  $ k < \infty $ since the remainder term in the lemma of 1.17 will not be a sum of products of  $ C^k $ functions, and the lemma doesn't even make sense in the  $ C^1 $ case. In fact, it turns out (see [21]) that  $ F_m/F_m^3 $ is always infinite dimensional in the  $ C^k $ case for  $ 1 \leq k < \infty $. There are various ways to define tangent vectors in the  $ C^k $ case in order that  $ \dim M_m = \dim M $ (all of which work in the  $ C^\infty $ case, too). One way is to define a tangent vector v at m as a mapping which assigns to each function (defined and differentiable of class  $ C^k $ on a neighborhood of m) a real number  $ v(f) $ such that if  $ (U, \varphi) $ is a coordinate system on a neighborhood of m, then there exists a list of real numbers  $ (a_1, \ldots, a_d) $ (depending on  $ \varphi $) such that

 $$ v(f)=\sum_{i=1}^{d}a_{i}\frac{\partial(f\circ\varphi^{-1})}{\partial r_{i}}\bigg|_{\varphi(m)}. $$ 

Then the space  $ M_m $ of tangent vectors again turns out to be finite dimensional, with a basis  $ \{(\partial/\partial x_i)\big|_{m}\} $.

1.22 The Differential Let  $ \psi: M \to N $ be  $ C^\infty $, and let  $ m \in M $. The differential of  $ \psi $ at  $ m $ is the linear map

 $$ d\psi\colon M_{m}\to N_{\psi(m)} $$ 

defined as follows. If $v\in M_{m}$, then $d\psi(v)$ is to be a tangent vector at $\psi(m)$, so we describe how it operates on functions. Let $g$ be a $C^{\infty}$ function on a neighborhood of $\psi(m)$. Define $d\psi(v)(g)$ by setting

 $$ d\psi(v)(g)=v(g\circ\psi). $$ 

It is easily checked that $d\psi$ is a linear map of $M_{m}$ into $N_{\psi(m)}$. Strictly speaking, this map should be denoted $d\psi\mid M_{m}$, or simply $d\psi_{m}$. However, we omit the subscript $m$ when there is no possibility of confusion. The map $\psi$ is called non-singular at $m$ if $d\psi_{m}$ is non-singular, that is, if the kernel of (1) consists of 0 alone. The dual map

 $$ (i.e.,(i n j.) $$ 

 $$ \delta\psi\colon N_{\psi(m)}^{*}\to M_{m}^{*} $$ 

is defined as usual by requiring that

 $$ \delta\psi(\omega)(v)=\omega\bigl(d\psi(v)\bigr) $$ 

whenever $\omega \in N_{v(m)}^{*}$ and $v \in M_{m}$. In the special case of a $C^{\infty}$ function $f: M \to \mathbb{R}$, if $v \in M_{m}$ and $f(m) = r_{0}$, then

 $$ d f(v)=v(f)\frac{d}{d r}\bigg|_{r_{0}}. $$ 

In this case, we usually take $df$ to mean the element of $M_{m}^{*}$ defined by

 $$ d f(v)=v(f). $$ 

That is, we identify $df$ with $\delta f(\omega)$, where $\omega$ is the basis of the 1-dimensional space $\mathbb{R}_{r_{0}}^{*}$ dual to $(d/dr)|_{r_{0}}$. Particular usage will be clear from the context.

### 1.23 Remarks on 1.22

(a) Let $(U, x_{1}, \ldots, x_{d})$ and $(V, y_{1}, \ldots, y_{t})$ be coordinate systems about $m$ and $\psi(m)$ respectively. Then it follows from 1.22(2) and 1.20(b) that

 $$ d\psi\left(\frac{\partial}{\partial x_{j}}\bigg|_{m}\right)=\sum_{i=1}^{\ell}\frac{\partial(y_{i}\circ\psi)}{\partial x_{j}}\bigg|_{m}\frac{\partial}{\partial y_{i}}\bigg|_{w(m)}. $$ 

The matrix $\{\partial(y_{i}\circ\psi)/\partial x_{i}\}$ is called the Jacobian of the map $\psi$ (with respect to the given coordinate system). For maps between Euclidean spaces, the Jacobian will always be taken with respect to the canonical coordinate systems.

(b) If $(U, x_1, \ldots, x_d)$ is a coordinate system on $M$, and $m \in U$, then $\{dx_i\}_{m}$ is the basis of $M_m^*$ dual to $\{\partial/\partial x_i\}_{m}\}$. If $f: M \to \mathbb{R}$ is a $C^\infty$ function, then

 $$ \begin{array}{r}{d f_{m}=\left.\sum_{i=1}^{d}\frac{\partial f}{\partial x_{i}}\right|_{m}d x_{i}|_{m}.}\end{array} $$ 

(c) Chain Rule. Let  $ \psi $:  $ M \to N $ and  $ \varphi $:  $ N \to X $ be  $ C^\infty $ maps. Then

 $$ d(\varphi\circ\psi)_{m}=d\varphi_{\psi(m)}\circ d\psi_{m}, $$ 

or simply $d(\varphi\circ\psi)=d\varphi\circ d\psi$. It is a useful exercise to check the form that this equation takes when the maps are expressed in terms of the matrices obtained by choosing coordinate systems.

(d) If $\psi: M \to N$ and $f: N \to \mathbb{R}$ are $C^\infty$, then $\delta\psi(df_{\psi(m)}) = d(f \circ \psi)_m$, for $\delta\psi(df_{\psi(m)})(v) = df(d\psi(v)) = d(f \circ \psi)_m(v)$ whenever $v \in M_m$.

(e) A $C^{\infty}$ mapping $\sigma: (a,b)\to M$ is called a smooth curve in $M$. Let $t\in(a,b)$. Then the tangent vector to the curve $\sigma$ at $t$ is the vector

 $$ d\sigma\left(\frac{d}{d r}\bigg|_{t}\right)\in M_{\sigma(t)}. $$ 

We shall denote the tangent vector to  $ \sigma $ at t by  $ \dot{\sigma}(t) $.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//775e6ebd-0f3f-4c72-ab2c-f2200f28e540/markdown_0/imgs/img_in_image_box_193_1012_798_1161.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A11Z%2F-1%2F%2Fcacfbdfb3f45300d8f1ba8658cf9d428a052ed89e64a9742b590ac1fd09df306" alt="Image" width="63%" /></div>

Now, if $v$ is any element of $M_{m}$, then $v$ is the tangent vector to a smooth curve in $M$. For one can simply choose a coordinate system $(U,\varphi)$, centered at $m$, for which

 $$ v=d\varphi\left(\frac{\partial}{\partial r_{1}}\bigg|_{0}\right). $$ 

Then $v$ is the tangent vector at 0 to the curve $t \mapsto \varphi^{-1}(t, 0, \ldots, 0)$. One should observe that many curves can have the same tangent vector, and that two smooth curves $\sigma$ and $\tau$ in $M$ for which $\sigma(t_{0}) = \tau(t_{0}) = m$ have the same tangent vector at $t_{0}$ if and only if

 $$ \frac{d(f\circ\sigma)}{d r}\Big|_{t_{0}}=\frac{d(f\circ\tau)}{d r}\Big|_{t_{0}} $$ 

for all functions $f$ which are $C^{\infty}$ on a neighborhood of $m$.

If $\sigma$ happens to be a curve in the Euclidean space $\mathbb{R}^{*}$, then

 $$ \dot{\sigma}(t)=\frac{d\sigma_{1}}{d r}\bigg|_{t}\frac{\partial}{\partial r_{1}}\bigg|_{\sigma(t)}+\cdots+\frac{d\sigma_{n}}{d r}\bigg|_{t}\frac{\partial}{\partial r_{n}}\bigg|_{\sigma(t)}. $$ 

If we identify this tangent vector with the element

 $$ \left(\frac{d\sigma_{1}}{d r}\bigg|_{t},\ldots,\frac{d\sigma_{n}}{d r}\bigg|_{t}\right) $$ 

of  $ R^{*} $, then we have

 $$ \dot{\sigma}(t)=\lim_{h\to0}\frac{\sigma(t+h)-\sigma(t)}{h}. $$ 

Thus with this identification our notion of tangent vector coincides, in this special case, with the geometric notion of a tangent to a curve in Euclidean space.

1.24 Theorem Let $\psi$ be a $C^\infty$ mapping of the connected manifold $M$ into the manifold $N$. Suppose that for each $m \in M$, $d\psi_m \equiv 0$. Then $\psi$ is a constant map.

PROOF Let $n\in\psi(M)$. $\psi^{-1}(n)$ is closed. We need only show that it is open. For this, let $m\in\psi^{-1}(n)$. Choose coordinate systems $(U,x_{1},\ldots,x_{d})$ and $(V,y_{1},\ldots,y_{c})$ about $m$ and $n$ respectively, so that $\psi(U)\subset V$. Then on $U$,

 $$ 0=d\psi\left(\frac{\partial}{\partial x_{j}}\right)=\sum_{i=1}^{c}\frac{\partial(y_{i}\circ\psi)}{\partial x_{j}}\frac{\partial}{\partial y_{i}}\qquad(j=1,\ldots,d), $$ 

which implies that

 $$ \frac{\partial(y_{i}\circ\psi)}{\partial x_{j}}\equiv0\qquad(i=1,\ldots,c;j=1,\ldots,d). $$ 

Thus the functions $y_{t}\circ\psi$ are constant on $U$. This implies that $\psi(U)=n$; hence $\psi^{-1}(n)$ is open and consequently $\psi^{-1}(n)=M$.

We shall now see that in a natural way the collection of all tangent vectors to a differentiable manifold itself forms a differentiable manifold called the tangent bundle. We have a similar dual object called the cotangent bundle formed from the linear functionals on the tangent spaces.

1.25 Tangent and Cotangent Bundles Let M be a $C^{\infty}$ manifold with differentiable structure $\mathcal{F}$. Let

 $$ \begin{aligned}{T(M)=\bigcup_{m\in\mathcal{M}}M_{m},}\\ {T^{*}(M)=\bigcup_{m\in\mathcal{M}}M_{m}^{*}.}\\ \end{aligned} $$ 

There are natural projections:

 $$ \begin{aligned}{\pi\colon T(M)\to M,\qquad}&{{}\pi(v)=m\quad\mathrm{i f}\quad v\in M_{m},}\\ {\pi^{*}\colon T^{*}(M)\to M,\qquad}&{{}\pi^{*}(\tau)=m\quad\mathrm{i f}\quad\tau\in M_{m}^{*}.}\\ \end{aligned} $$ 

Let $(U,\varphi)\in\mathcal{F}$ with coordinate functions $x_1,\ldots,x_d$. Define $\tilde{\varphi}\colon\pi^{-1}(U)\to\mathbb{R}^{2d}$ and $\tilde{\varphi}^*colon(U)\to\mathbb{R}^{2d}$ by

 $$ \tilde{\varphi}(v)=\big(x_{1}\big(\pi(v)\big),\ldots,x_{d}\big(\pi(v)\big),d x_{1}(v),\ldots,d x_{d}(v)\big) $$ 

 $$ \tilde{\varphi}^{*}(\tau)=\Bigl(x_{1}\bigl(\pi^{*}(\tau)\bigr),\ldots,x_{d}\bigl(\pi^{*}(\tau)\bigr),\tau\Bigl(\frac{\partial}{\partial x_{1}}\Bigr),\ldots,\tau\Bigl(\frac{\partial}{\partial x_{d}}\Bigr)\Bigr) $$ 

for all $v\in\pi^{-1}(U)$ and $\tau\in(\pi^{*})^{-1}(U)$. Note that $\widetilde{\varphi}$ and $\widetilde{\varphi}^*$ are both one-to-one maps onto open subsets of $\mathbb{R}^{2d}$. The following steps outline the construction of a topology and a differentiable structure on $T(M)$. The construction for $T^*(M)$ goes similarly. The proofs are left as exercises.

(a) If  $ (U,\varphi) $ and  $ (V,\varphi)\in\mathcal{F} $, then  $ \tilde{\psi}\circ\tilde{\varphi}^{-1} $ is  $ C^{\infty} $.

(b) The collection $\{\tilde{\varphi}^{-1}(W)\colon W \text{ open in } \mathbb{R}^{2d}, (U,\varphi) \in \mathcal{F}\}$ forms a basis for a topology on $T(M)$ which makes $T(M)$ into a $2d$-dimensional, second countable, locally Euclidean space.

(c) Let $\mathcal{F}$ be the maximal collection, with respect to 1.4(b), containing

 $$ \{(\pi^{-1}(U),\widetilde{\varphi})\colon(U,\varphi)\in\mathcal{F}\}. $$ 

Then $\mathcal{F}$ is a differentiable structure on $T(M)$.

$T(M)$ and $T^{*}(M)$ with these differentiable structures are called respectively the tangent bundle and the cotangent bundle. It will sometimes be convenient to write the points of $T(M)$ as pairs $(m,v)$ where $m\in M$ and $v\in M_{m}$ (and similarly for $T^{*}(M)$).

If $\psi: M \to N$ is a $C^{\infty}$ map, then the differential of $\psi$ defines a mapping of the tangent bundles

 $$ d\psi\colon T(M)\to T(N), $$ 

where  $ d\psi(m,v) = d\psi_{m}(v) $ whenever  $ v \in M_{m} $. It is easily checked that (4) is a  $ C^{\infty} $ map.

1.26† Higher Order Tangent Vectors and Differentials It is useful to look at $M_{m}$ as $(F_{m}/F_{m}^{2})^{*}$, for this point of view allows an immediate generalization to higher order tangent vectors. We digress for a moment to give these definitions.

Recall that  $ \tilde{F}_{m} $ is the algebra of germs of functions at m.  $ \tilde{F}_{m} \subset \tilde{F}_{m} $ is the ideal of germs vanishing at m, and  $ \tilde{F}_{m}^{k} $ (k an integer  $ \geq 1 $) is the ideal of  $ \tilde{F}_{m} $ consisting of all finite linear combinations of k-fold products of elements of  $ \tilde{F}_{m} $.

The vector space $F_m/F_m^{\kappa+1}$ is called the space of $k$th order differentials at $m$, and we denote it by $^k M_m$. As before, $f$ denotes the germ of $f$ at $m$, and {} will denote cosets in $F_m/F_m^{\kappa+1}$. Let $f$ be a differentiable function on a neighborhood of $m$. We define the $k$th order differential $d^k f$ of $f$ at $m$ by

 $$ d^{k}f=\{\mathbf{f}-\mathbf{f}(\mathbf{m})\}. $$ 

A kth order tangent vector at m is a real linear function on  $ F_{m} $ vanishing on  $ F_{m}^{k+1} $ and vanishing also on the set of germs of functions constant on a neighborhood of m. The real linear space of kth order tangent vectors at m will be denoted by  $ M_{m}^{k} $. We have a natural identification of  $ M_{m}^{k} $ with  $ (kM_{m})^{*} $ since any kth order tangent vector restricted to  $ F_{m} $ yields a linear function on  $ F_{m} $ vanishing on  $ F_{m}^{k+1} $, and hence yields an element of  $ (kM_{m})^{*} $; and conversely an element of  $ (kM_{m})^{*} $ uniquely determines a linear function on  $ F_{m} $ vanishing on  $ F_{m}^{k+1} $, and this extends uniquely to a kth order tangent vector by requiring it to annihilate germs of constant functions.

We can tie up this notion of higher order tangent vector with the usual notion of higher order derivative in Euclidean space by looking at the forms that these tangent vectors and differentials take in a coordinate system. Let  $ (U,\varphi) $ be a coordinate system about  $ m $ with coordinate functions  $ x_1, \ldots, x_d $ such that  $ \varphi(U) $ is a convex open set in Euclidean space  $ \mathbb{R}^d $. Let  $ \alpha = (\alpha_1, \ldots, \alpha_d) $ be a list of non-negative integers. In addition to our conventions of 1.1, we let

 $$ (x-x(m))^{\alpha}=(x_{1}-x_{1}(m))^{\alpha_{1}}\cdots(x_{d}-x_{d}(m))^{\alpha_{d}}. $$ 

Let f be a  $ C^{\infty} $ function on U. Then it follows from the lemma of 1.17, that

 $$ f=f(m)+\sum_{\{\alpha\}=1}^{k}a_{\alpha}(x-x(m))^{\alpha}+\sum_{\{\alpha\}=k+1}h_{\alpha}(x-x(m))^{\alpha}, $$ 

The material of this section will not be used elsewhere in the book, and so it may be skipped without loss of continuity.

where the $h_{\alpha}$ are $C^{\infty}$ functions on $U$ and where

 $$ a_{\alpha}=\frac{1}{\alpha!}\frac{\partial^{\alpha}(f\circ\varphi^{-1})}{\partial r^{\alpha}}\bigg|_{\varphi(m)}. $$ 

Hence

 $$ d^{k}f=\sum_{1\leq[\alpha]\leq k}a_{\alpha}\{\left(\mathbf{x}-\mathbf{x}(\mathbf{m})\right)^{\alpha}\}. $$ 

Thus the collection

 $$ [\{(x-\mathbf{x}(\mathbf{m}))^{a}\}\colon1\leq[\alpha]\leq k] $$ 

spans  $ ^{k}M_{m} $. The proof that these elements are linearly independent in  $ ^{k}M_{m} $ is the obvious generalization of the proof for the case k = 2 which was treated in 1.17. Thus the collection (5) forms a basis of  $ ^{k}M_{m} $. Consequently  $ ^{k}M_{m} $ is finite dimensional with dimension equal to the binomial coefficient  $ \sum_{j=1}^{k}\binom{d+j-1}{j} $. As the dual space of  $ ^{k}M_{m} $,  $ M_{m}^{k} $ is also finite dimensional with the same dimension. Since  $ M_{m}^{k} $ is identified with  $ (^{k}M_{m})^{*} $, and these spaces are finite dimensional, we have a canonical isomorphism of  $ ^{k}M_{m} $ with  $ (M_{m}^{k})^{*} $, under which the element of  $ d^{k}f \in ^{k}M_{m} $, considered as an element of  $ (M_{m}^{k})^{*} $, satisfies

 $$ d^{k}f(v)=v(\mathbf{f}). $$ 

Let

 $$ \frac{\partial^{\alpha}f}{\partial x^{\alpha}}\bigg|_{m}=\frac{\partial^{\alpha}(f\circ\varphi^{-1})}{\partial r^{\alpha}}\bigg|_{\varphi(m)}. $$ 

Since the derivative is linear, and since the value of $\partial^a f/\partial x^a$ at $m$ depends only on the germ of $f$ at $m$ and vanishes if $f$ is constant on a neighborhood of $m$ or if $f$ is an $[\alpha]+1$-fold product of functions which vanish at $m$, then $(\partial^a/\partial x^a)\big|_m$ is an $[\alpha]$th order tangent vector at $m$. It follows that

 $$ \left\{\left(\frac{1}{\alpha!}\right)\frac{\partial^{\alpha}}{\partial x^{\alpha}}\bigg|_{m}:1\leq[\alpha]\leq k\right\} $$ 

is the basis of $M_{m}^{k}$ dual to the basis (5) of $^{k}M_{m}$. If $v$ is a $k$th order tangent vector at $m$, then

 $$ v=\sum_{[a]=1}^{k}b_{a}\frac{\partial^{a}}{\partial x^{a}}\bigg|_{m}, $$ 

where

 $$ b_{\alpha}=\left(\frac{1}{\alpha!}\right)v(({\bf x}-{\bf x}({\bf m}))^{\alpha}). $$ 

In terms of the basis (8), equation (3) becomes

 $$ a_{a}=\frac{1}{\alpha!}\frac{\partial^{a}f}{\partial x^{\alpha}}\bigg|_{m}. $$ 

As in the case of first order tangent vectors, we customarily think of tangent vectors as operating on the functions themselves rather than their germs; indeed, we define

 $$ v(f)=v(\mathbf{f}) $$ 

whenever $f$ is $C^{\infty}$ on a neighborhood of $m$ and $v$ is a tangent vector of any order at $m$.

Finally, just as there are natural mappings of tangent vectors and differentials associated with a differentiable map $\varphi\colon M\to N$, so are there linear mappings

 $$ \begin{aligned}{}&{{}d^{k}\varphi\colon M_{m}{}^{k}\to N_{\varphi(m)}^{k},}\\ {}&{{}\delta^{k}\varphi\colon{}^{k}N_{\varphi(m)}\to{}^{k}M_{m}}\\ \end{aligned} $$ 

defined by

 $$ \begin{array}{c}{d^{k}\varphi(v)(g)=v(g\circ\varphi),}\\ {\partial^{k}\varphi(d^{k}g)=d^{k}(g\circ\varphi)}\\ \end{array} $$ 

whenever $v\in M_{m}^{k}$ and $g$ is a $C^{\infty}$ function on a neighborhood of $\varphi(m)$. It is easily checked that (14) does indeed define the mappings (13) and that the mappings $d^{k}\varphi$ and $\delta^{k}\varphi$ are dual.

Our definition of a first order tangent vector in this section agrees with Definition 1.14 in view of Lemma 1.16. Moreover, we have seen three interpretations of the first order differential $df$ of a function $f$; the interpretation (13) agrees with our original definition 1.22(1), the interpretation (6) agrees with 1.22(6), and we have the additional interpretation (1).

## SUBMANIFOLDS, DIFFEOMORPHISMS, AND THE INVERSE FUNCTION THEOREM

1.27 Definitions Let  $ \psi\colon M \to N $ be  $ C^\infty $.

(a)  $ \psi $ is an immersion if  $ d\psi_{m} $ is non-singular for each  $ m \in M $.

(b) The pair $(M,\psi)$ is a submanifold of $N$ if $\psi$ is a one-to-one immersion.

(c)  $ \psi $ is an imbedding if  $ \psi $ is a one-to-one immersion which is also a homeomorphism into; that is,  $ \psi $ is open as a map into  $ \psi(M) $ with the relative topology.

(d)  $ \psi $ is a diffeomorphism if  $ \psi $ maps  $ M $ one-to-one onto  $ N $ and  $ \psi^{-1} $ is  $ C^\infty $.

1.28 Remarks on 1.27 One can, for example, immerse the real line R into the plane, as illustrated in the following figure, so that the first case is an immersion which is not a submanifold, the second is a submanifold which is not an imbedding, and the third is an imbedding.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//84cfd649-485a-47cc-b27b-fb4ff71ab8f1/markdown_2/imgs/img_in_image_box_128_118_775_372.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A22Z%2F-1%2F%2Fd69daef1650dd84204875a5e6ccbf781c6ab8b6297f97a5056bb487365fade55" alt="Image" width="68%" /></div>

Immersion, but not a Submanifold

Submanifold, but not an Imbedding

Imbedding

Observe that if $(U,\varphi)$ is a coordinate system, then $\varphi\colon U\to\varphi(U)$ is a diffeomorphism.

The composition of diffeomorphisms is again a diffeomorphism. Thus the relation of being diffeomorphic is an equivalence relation on the collection of differentiable manifolds. It is quite possible for a locally Euclidean space to possess distinct differentiable structures which are diffeomorphic. (See Exercise 2.) In a remarkable paper, Milnor showed the existence of locally Euclidean spaces ($S^{7}$ is an example) which possess non-diffeomorphic differentiable structures [19]. There are also locally Euclidean spaces which possess no differentiable structures at all [14].

If $\psi$ is a diffeomorphism, then $d\psi_m$ is an isomorphism since both $(d\psi \circ d\psi^{-1})|_{\psi(m)}$ and $(d\psi^{-1} \circ d\psi)|_m$ are the identity transformations. The inverse function theorem gives us a local converse of this—whenever $d\psi_m$ is an isomorphism, $\psi$ is a diffeomorphism on a neighborhood of $m$. Before we recall the precise statement of the inverse function theorem, we give a definition which will be needed in the corollaries.

1.29 Definition A set $y_{1}, \ldots, y_{i}$ of $C^{\infty}$ functions defined on some neighborhood of $m$ in $M$ is called an independent set at $m$ if the differentials $dy_{1}, \ldots, dy_{i}$ form an independent set in $M_{m}^{*}$.

1.30 Inverse Function Theorem Let  $ U \subset \mathbb{R}^d $ be open, and let  $ f: U \to \mathbb{R}^d $ be  $ C^\infty $. If the Jacobian matrix

 $$ \left\{\frac{\partial r_{i}\circ f}{\partial r_{j}}\right\}_{i,j=1,\ldots,d} $$ 

is non-singular at  $ r_0 \in U $, then there exists an open set  $ V $ with  $ r_0 \in V \subset U $ such that  $ f \mid V $ maps  $ V $ one-to-one onto the open set  $ f(V) $, and  $ (f \mid V)^{-1} $ is  $ C^\infty $.

This is one of the results we shall assume from advanced calculus. For a proof, we refer the reader, for example, to [31] or [6].

##### Manifolds

Corollary (a) Assume that $\psi: M \to N$ is $C^{\infty}$, that $m \in M$, and that $d\psi: M_{m} \to N_{\psi(m)}$ is an Isomorphism. Then there is a neighborhood $U$ of $m$ such that $\psi: U \to \psi(U)$ is a diffeomorphism onto the open set $\psi(U)$ in $N$.

PROOF Observe that $\dim M = \dim N$, say $d$. Choose coordinate systems $(V, \varphi)$ about $m$ and $(W, \tau)$ about $\varphi(m)$ with $\varphi(V) \subset W$. Let $\varphi(m) = p$ and $\tau(\varphi(m)) = q$. The differential of the map $\tau \circ \varphi \circ \varphi^{-1} \mid \varphi(V)$ is non-singular at $p$. Thus the inverse function theorem yields a diffeomorphism $\alpha: \tilde{U} \to \alpha(\tilde{U})$ on a neighborhood $\tilde{U}$ of $p$ with $\tilde{U} \subset \varphi(V)$. Then $\tau^{-1} \circ \alpha \circ \varphi$ is the required diffeomorphism on the neighborhood $U = \varphi^{-1}(\tilde{U})$ of $m$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//84cfd649-485a-47cc-b27b-fb4ff71ab8f1/markdown_3/imgs/img_in_image_box_173_372_781_655.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A23Z%2F-1%2F%2F6ff03c55b62496e4752ebad6c45af85138b30c6126dbfd5aa4a758f8cec58703" alt="Image" width="61%" /></div>

Corollary (b) Suppose that $\dim M = d$ and that $y_1, \ldots, y_d$ is an independent set of functions at $m_0 \in M$. Then the functions $y_1, \ldots, y_d$ form a coordinate system on a neighborhood of $m_0$.

PROOF Suppose that the $y_i$ are defined on the open set $U$ containing $m_0$. Define $\psi: U \to \mathbb{R}^d$ by

 $$ \psi(m)=\left(y_{1}(m),\ldots,y_{d}(m)\right)\qquad(m\in U). $$ 

Then  $ \psi $ is  $ C^{\infty} $. Now  $ \delta\psi $ is an isomorphism on  $ (\mathbb{R}_{\psi(m_{a})}^{d})^{*} $ since

 $$ \delta\varphi(d r_{i})=d(r_{i}\circ\varphi)=d y_{i} $$ 

which implies that  $ \delta\psi\big|_{\psi(m_0)} $ takes a basis to a basis. Consequently, the differential  $ d\psi_{m_0} $ (which is the dual of  $ \delta\psi\big|_{\psi(m_0)} $) is an isomorphism. So the inverse function theorem implies that  $ \psi $ is a diffeomorphism on a neighborhood  $ V \subset U $ of  $ m_0 $, and consequently the functions  $ y_1, \ldots, y_d $ yield a coordinate system when restricted to V.

Corollary (c) Suppose that $\dim M = d$ and that $y_{1}, \ldots, y_{1}$, with $l < d$, is an independent set of functions at $m$. Then they form part of a coordinate system on a neighborhood of $m$.

PROOF Let $(U, x_1, \ldots, x_d)$ be a coordinate system about $m$. Then $\{dy_1, \ldots, dy_i, dx_1, \ldots, dx_d\}$ spans $M_m^*$. Choose $d-l$ of the $x_i$ so that $\{dy_1, \ldots, dy_i, dx_{i_1}, \ldots, dx_{i_{d-1}}\}$ is a basis of $M_m^*$. Then apply Corollary (b).

Corollary (d) Let $\psi: M \to N$ be $C^{\infty}$, and assume that $d\psi: M_{m} \to N_{\psi(m)}$ is surjective. Let $x_{1}, \ldots, x_{1}$ form a coordinate system on some neighborhood of $\psi(m)$. Then $x_{1} \circ \psi, \ldots, x_{1} \circ \psi$ form part of a coordinate system on some neighborhood of $m$.

PROOF The fact that $d\psi_{m}$ is surjective implies that the dual map $\delta\psi|_{v(m)}$ is injective. Thus the functions $\{x_{i}\circ\psi:i=1,\ldots,l\}$ are independent at $m$ since $\delta\psi(dx_{i})=d(x_{i}\circ\psi)$. The claim now follows from Corollary (c).

Corollary (e) Suppose that $y_{1},\ldots,y_{k}$ is a set of $C^{\infty}$ functions on a neighborhood of $m$ such that their differentials span $M_{m}^{*}$. Then a subset of the $y_{i}$ forms a coordinate system on a neighborhood of $m$.

PROOF Simply choose a subset whose differentials form a basis of  $ M_{m}^{*} $, and apply Corollary (b).

Corollary (f) Let $\psi: M \to N$ be $C^{\infty}$, and assume that $d\psi: M_{m} \to N_{\psi(m)}$ is injective. Let $x_{1}, \ldots, x_{k}$ form a coordinate system on a neighborhood of $\psi(m)$. Then a subset of the functions $\{x_{i} \circ \psi\}$ forms a coordinate system on a neighborhood of $m$. In particular, $\psi$ is one-to-one on a neighborhood of $m$.

PROOF The fact that $d\psi_m$ is injective implies that $\delta\psi|_{\psi(m)}$ is surjective. This implies that $\{d(x_i \circ \psi) = \delta\psi(dx_i): i = 1, \ldots, k\}$ spans $M_m^*$. This corollary then follows from Corollary (e).

1.31 The situation often arises that one has a $C^{\infty}$ mapping, say $\psi$, of a manifold $N$ into a manifold $M$ factoring through a submanifold $(P,\varphi)$ of $M$. That is, $\psi(N) \subset \varphi(P)$, whence there is a uniquely defined mapping $\psi_0$ of $N$ into $P$ such that $\varphi \circ \psi_0 = \psi$. The problem is: When is $\psi_0$ of class $C^{\infty}$? This is certainly not always the case. As an example, let $N$ and $P$ both be the real line, and let $M$ be the plane. Let $(\mathbb{R},\psi)$ and $(\mathbb{R},\varphi)$ both be figure-8 submanifolds with precisely the same image sets, but with the difference that as $t \to \pm \infty$, $\psi(t)$ approaches the intersection along the horizontal direction, but $\varphi(t)$ approaches along the vertical. Suppose also that $\psi(0) = \varphi(0) = 0$. Then $\psi_0$ is not even continuous since $\psi_0^{-1}(-1,1)$ consists of the origin plus two open sets of the form $(\alpha,+\infty)$, $(-\infty,-\alpha)$ for some $\alpha > 0$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//c39f73a5-46d9-4f67-96a1-7149c914d027/markdown_0/imgs/img_in_image_box_153_1038_578_1216.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A26Z%2F-1%2F%2F62a19391c8cb30e9da0ec000f85b3aa8252dcd22eadef9d695181b7bc332824a" alt="Image" width="44%" /></div>

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//c39f73a5-46d9-4f67-96a1-7149c914d027/markdown_0/imgs/img_in_image_box_615_1044_813_1171.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A26Z%2F-1%2F%2Fa7927a52a7137dfd1c82687293f1e0d99dad474edf535e42a4883c96c248d106" alt="Image" width="20%" /></div>

1.32 Theorem Suppose that $\psi: N \to M$ is $C^\infty$, that $(P, \varphi)$ is a submanifold of $M$, and that $\varphi$ factors through $(P, \varphi)$, that is, $\psi(N) \subset \varphi(P)$. Since $\varphi$ is injective, there is a unique mapping $\psi_0$ of $N$ into $P$ such that $\varphi \circ \varphi_0 = \varphi$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//c39f73a5-46d9-4f67-96a1-7149c914d027/markdown_1/imgs/img_in_image_box_346_196_547_325.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A28Z%2F-1%2F%2F6b01c3effd7538a62fbc1e33270dc28406135b8b1d3a5f3d83061f515c9ac295" alt="Image" width="20%" /></div>

(a)  $ \psi_{0} $ is  $ C^{\infty} $ if it is continuous.

(b)  $ \psi_{0} $ is continuous if  $ \varphi $ is an imbedding.

Another important case in which  $ \varphi_{0} $ is continuous occurs when  $ (P,\varphi) $ is an integral manifold of an involutive distribution on M, as we shall see in 1.62.

PROOF Result (b) is obvious. So assume that $\psi_0$ is continuous. We prove that it is $C^\infty$. It suffices to show that $P$ can be covered by coordinate systems $(U,\tau)$ such that the map $\tau\circ\psi_0$ restricted to the open set $\psi_0^{-1}(U)$ is $C^\infty$. Let $p\in P$, and let $(V,\gamma)$ be a coordinate system on a neighborhood of $\varphi(p)$ in $M^d$. Then by Corollary (f) of 1.30 there exists a projection $\pi$ of $\mathbb{R}^d$ onto a suitable subspace (obtained by setting certain of the coordinate functions equal to $0$) such that the map $\tau=\pi\circ\gamma\circ\varphi$ yields a coordinate system on a neighborhood $U$ of $p$. Then

 $$ \begin{aligned}{\tau\circ\psi_{\emptyset}\mid\psi_{\emptyset}^{-1}(U)}&{{}=\pi\circ\gamma\circ\varphi\circ\psi_{\emptyset}\mid\psi_{\emptyset}^{-1}(U)}\\ {}&{{}=\pi\circ\gamma\circ\psi\mid\psi_{\emptyset}^{-1}(U),}\\ \end{aligned} $$ 

which is  $ C^{\infty} $

1.33 Further Remarks on Submanifolds Submanifolds  $ (N_{1},\varphi_{1}) $ and  $ (N_{2},\varphi_{2}) $ of M will be called equivalent if there exists a diffeomorphism  $ \alpha\colon N_{1}\to N_{2} $ such that  $ \varphi_{1}=\varphi_{2}\circ\alpha $.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//c39f73a5-46d9-4f67-96a1-7149c914d027/markdown_1/imgs/img_in_image_box_345_900_553_1026.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A29Z%2F-1%2F%2F4e85340033c1ee7082cc74b459bb075ea5d3295abc64bf5c2a690785967ebf4c" alt="Image" width="21%" /></div>

This is an equivalence relation on the collection of all submanifolds of $M$. Each equivalence class $\xi$ has a unique representative of the form $(A,i)$ where $A$ is a subset of $M$ with a manifold structure such that the inclusion map $i: A \to M$ is a $C^\infty$ immersion. Namely, if $(N,\varphi)$ is any representative

of $\xi$, then the subset $A$ of $M$ must be $\varphi(N)$. We induce a manifold structure on $A$ by requiring $\varphi: N \to A$ to be a diffeomorphism. With this manifold structure, $(A,i)$ is a submanifold of $M$ equivalent to $(N,\varphi)$. This is the only manifold structure on $A$ with the property that $(A,i)$ is equivalent to $(N,\varphi)$; thus this is the unique such representative of $\xi$.

The conclusion of some theorems in the following sections states that there exist unique submanifolds satisfying certain conditions. Uniqueness means up to equivalence as defined above. In particular, if the submanifolds of $M$ are viewed as subsets $A \subset M$ with manifold structures for which the inclusion maps are $C^{\infty}$ immersions, then uniqueness means unique subset with unique second countable locally Euclidean topology and unique differentiable structure.

In the case of a submanifold $(A,i)$ of $M$ where $i$ is the inclusion map, we shall often drop the $i$ and simply speak of the submanifold $A \subset M$.

Let $A$ be a subset of $M$. Then generally there is not a unique manifold structure on $A$ such that $(A,l)$ is a submanifold of $M$, if there is one at all. For example, the diagrams in 1.31 illustrate two distinct manifold structures on the figure-8 in the plane, each of which makes the figure-8 together with the inclusion map a submanifold of $\mathbb{R}^{2}$. However, we have the following two uniqueness theorems which involve conditions on the topology on $A$.

(a) Let $M$ be a differentiable manifold and $A$ a subset of $M$. Fix a topology on $A$. Then there is at most one differentiable structure on $A$ such that $(A, i)$ is a submanifold of $M$, where $i$ is the inclusion map.

(b) Again let $A$ be a subset of $M$. If in the relative topology, $A$ has a differentiable structure such that $(A,i)$ is a submanifold of $M$, then $A$ has a unique manifold structure (that is, unique second countable locally Euclidean topology together with a unique differentiable structure) such that $(A,i)$ is a submanifold of $M$.

We leave these to the reader as exercises. Result (a) follows from an application of Theorem 1.32. Result (b) depends strongly on our assumption that manifolds are second countable, and for its proof you will need to use the proposition in Exercise 6 in addition to Theorem 1.32.

1.34 Slices Suppose that $(U,\varphi)$ is a coordinate system on $M$ with coordinate functions $x_1,\ldots,x_d$, and that $c$ is an integer, $0\leq c\leq d$. Let $a\in\varphi(U)$, and let

 $$ S=\{q\in U\colon x_{i}(q)=\mathbb{X}_{i}(a),i=c+1,\ldots,d\}. $$ 

The subspace S of M together with the coordinate system

 $$ \{x_{i}\mid S\colon j=1,\ldots,c\} $$ 

forms a manifold which is a submanifold of $M$ called a slice of the coordinate system $(U, \varphi)$.

1.35 Proposition Let $\psi: M^{c} \to N^{d}$ be an immersion, and let $m \in M$. Then there exists a cubic-centered coordinate system $(V, \varphi)$ about $\psi(m)$ and a neighborhood $U$ of $m$ such that $\psi \mid U$ is 1:1 and $\psi(U)$ is a slice of $(V, \varphi)$.

PROOF Let $(W,\tau)$ be a centered coordinate system about $\psi(m)$ with coordinate functions $y_{1},\ldots,y_{d}$. By Corollary (f) of 1.30 we can renumber the coordinate functions so that

 $$ \tilde{\tau}=\pi_{a}\circ\tau\circ\psi $$ 

is a coordinate map on a neighborhood $V'$ of $m$ where $\pi_e\colon\mathbb{R}^d\to\mathbb{R}^e$ is projection on the first $c$ coordinates. Define functions $\{x_t\}$ on $(\pi_e\circ\tau)^{-1}(\tilde{\tau}(V'))$ by setting

 $$ x_{i}=\left\{\begin{aligned}{}&{{}y_{i}}&{}&{{}(i=1,\ldots,c)}\\ {}&{{}y_{i}-y_{i}\circ\psi\circ\tilde{\tau}^{-1}\circ\pi_{c}\circ\tau}&{}&{{}(i=c+1,\ldots,d).}\\ \end{aligned}\right. $$ 

The functions $\{x_{t}\}$ are independent at $\psi(m)$, since at $\psi(m)$,

 $$ d x_{i}=\left\{\begin{aligned}{}&{{}d y_{i}}&{}&{{}(i=1,\ldots,c)}\\ {}&{{}d y_{i}+\sum_{s=1}^{c}a_{i j}d y_{j}}&{}&{{}(i=c+1,\ldots,d)}\\ \end{aligned}\right. $$ 

for some constants $a_{ij}$. By Corollary (b) of 1.30 the $\{x_i\}$ form a coordinate system on a neighborhood of $\psi(m)$. Let $V$ be a neighborhood of $\psi(m)$ on which the $x_1, \ldots, x_d$ form a cubic coordinate system. Denote the corresponding coordinate map by $\varphi$. Let $U = \psi^{-1}(V) \cap V$. Then $U$ and $(V, \varphi)$ are the required neighborhood and coordinate system.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//c39f73a5-46d9-4f67-96a1-7149c914d027/markdown_3/imgs/img_in_image_box_122_729_777_1178.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A31Z%2F-1%2F%2Fcb834f6e4bfd97b811d4e74586a7268e15601db460b613d89f3581b62c017674" alt="Image" width="66%" /></div>

We emphasize that this proposition only says that there is a neighborhood $U$ of $m$ such that $\psi(U)$ is a slice of the coordinate system $(V,\varphi)$. Even if $(M,\psi)$ is a submanifold of $N$, it may well be that $\psi(M)\cap V$ is far from being a slice or even a union of slices. For an example, consider again the figure-8 submanifold of the plane:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//cfd2d4f8-2f72-4986-81e3-8d0f6ee731af/markdown_0/imgs/img_in_image_box_131_248_790_491.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A11Z%2F-1%2F%2Fe8f638f81df0e233e4d2bdcd55c43566bfd3a922ac5fa9695996d31b3b08c423" alt="Image" width="69%" /></div>

However, in the case that $(M,\psi)$ is an imbedded submanifold, the coordinate system $(V,\varphi)$ can be chosen so that all of $\psi(M)\cap V$ is a single slice of $V$.

Let us now consider the question of the extent to which the set of $C^{\infty}$ functions on a manifold determines the set of $C^{\infty}$ functions on a submanifold. Let $(M,\psi)$ be a submanifold of $N$. Then, of course, if $f\in C^{\infty}(N)$, then $f|M$ is a $C^{\infty}$ function on $M$. (More precisely, $f\circ\psi$ is a $C^{\infty}$ function on $M$) In general, however, the converse does not hold; that is, not all $C^{\infty}$ functions on $M$ arise as the restrictions to $M$ of $C^{\infty}$ functions on $N$. For the converse to hold, it is necessary and sufficient to assume that $\psi$ is an imbedding and that $\psi(M)$ is closed. We prove the sufficiency in the following proposition, and leave the necessity as Exercise 11 below.

1.36 Proposition Let $\psi: M \to N$ be an imbedding such that $\psi(M)$ is closed in $N$. If $g \in C^{\infty}(M)$, then there exists $f \in C^{\infty}(N)$ such that $f \circ \psi = g$.

To simplify notation, we shall suppress the map $\psi$ and consider $M \subset N$.

PROOF For each point $p \in M$ there exists an open set $O_p$ in $N$ containing $p$ and an extension of $g$ from $O_p \cap M$ to a $C^\infty$ function $\tilde{g}_p$ on $O_p$. One simply has to take $O_p$ to be a cubic-centered coordinate neighborhood of $p$ for which $M \cap O_p$ is a single slice, and then define $\tilde{g}_p$ to be the composition of the natural projection of $O_p$ onto the slice followed by $g$. The collection $\{O_p : p \in M\}$ together with $N - M$ forms an open cover of $N$. By Theorem 1.11, there exists a partition of unity $\{\varphi_i\}$, with $j = 1, 2, \ldots$, subordinate to this cover. Take the subsequence (which we shall continue to denote by $\{\varphi_i\}$) such that supp $\varphi_i \cap M \neq \emptyset$. For each such $j$, we can choose a point $p_i$ such that supp $\varphi_i \subset O_{p_i}$. Then $f = \sum_{j} \varphi_i \tilde{g}_{p_i}$ is a $C^\infty$ function on $N$, and $f \mid M = g$.

##### IMPLICIT FUNCTION THEOREMS

From the inverse function theorem we shall obtain two theorems which will provide us with an extremely useful way of proving that certain subsets of manifolds are submanifolds. Under suitable conditions on a differentiable map, the inverse image of a submanifold of its range will be a submanifold of its domain. We first recall the statement of the classical implicit function theorem. This is simply a local (but somewhat more explicit) version of the first "implicit function" theorem (1.38) that we shall prove for manifolds. We suggest that the reader supply a proof of 1.37 after reading 1.38.

1.37 Implicit Function Theorem Let  $ U \subset \mathbb{R}^{e-d} \times \mathbb{R}^{d} $ be open, and let  $ f: U \to \mathbb{R}^{d} $ be  $ C^{\infty} $. We denote the canonical coordinate system on  $ \mathbb{R}^{e-d} \times \mathbb{R}^{d} $ by  $ (r_{1}, \ldots, r_{e-d}, s_{1}, \ldots, s_{d}) $. Suppose that at the point  $ (r_{0}, s_{0}) \in U $

 $$ f(r_{0},s_{0})=0, $$ 

and that the matrix

 $$ \left\{\frac{\partial f_{i}}{\partial s_{j}}\bigg|_{(r_{0},s_{0})}\right\}_{i,j=1,\ldots,d} $$ 

is non-singular. Then there exists an open neighborhood $V$ of $r_0$ in $\mathbb{R}^{s-d}$ and an open neighborhood $W$ of $s_0$ in $\mathbb{R}^d$ such that $V \times W \subset U$, and there exists a $C^\infty$ map $g: V \to W$ such that for each $(p,q) \in V \times W$

 $$ f(p,q)=0\;\:\leftrightarrow\;q=g(p). $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//cfd2d4f8-2f72-4986-81e3-8d0f6ee731af/markdown_1/imgs/img_in_image_box_158_769_735_1115.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A12Z%2F-1%2F%2F12413bed76d0a04870a665bf0aca6b65b9d4d4872e0ede15892bc2422834ff98" alt="Image" width="58%" /></div>

1.38 Theorem Assume that $\Psi: M^{c} \to N^{d}$ is $C^{\infty}$, that $n$ is a point of $N$, that $P = \psi^{-1}(n)$ is non-empty, and that $d\psi: M_{m} \to N_{\psi(m)}$ is surjective for all $m \in P$. Then $P$ has a unique manifold structure such that $(P, i)$ is a submanifold of $M$, where $i$ is the inclusion map. Moreover, $i: P \to M$ is actually an imbedding, and the dimension of $P$ is $c - d$.

PROOF According to result (b) of 1.33, it is sufficient to prove that in the relative topology, $P$ has a differentiable structure such that $(P,i)$ is a submanifold of $M$ of dimension $c-d$. For this it is sufficient to prove that if $m\in P$, then there exists a coordinate system on a neighborhood $U$ of $m$ in $M$ for which $P\cap U$ is a single slice of the correct dimension. Let $x_{1},\ldots,x_{d}$ be a coordinate system centered at $n$ in $N$. Then since $d\psi:M_{m}\to N_{n}$ is surjective, it follows from Corollary (d) of 1.30 that the collection of functions

 $$ \{y_{i}=x_{i}\circ\psi\colon i=1,\ldots,d\}, $$ 

forms part of a coordinate system about $m\in M$. Complete to a coordinate system $y_1,\ldots,y_d,y_{d+1},\ldots,y_c$ on a neighborhood $U$ of $m$. Then $P\cap U$ is precisely the slice of this coordinate system given by

 $$ y_{1}=y_{2}=\cdots=y_{d}=0. $$ 

In this theorem the inverse image of a point is shown to be a submanifold as long as the differential is surjective at each point of the inverse image. A point can be thought of as a 0-dimensional submanifold. We now generalize this theorem by proving that under suitable conditions the inverse images of higher dimensional submanifolds are themselves submanifolds.

1.39 Theorem Assume that $\psi: M \to N^d$ is $C^\infty$ and that $(O^c, \varphi)$ is a submanifold of $N$. Suppose that whenever $m \in \psi^{-1}\left(\varphi(O)\right)$, then

 $$ N_{\psi(m)}=d\psi(M_{m})+d\varphi(O_{\psi^{-1}(\psi(m))}) $$ 

(not necessarily a direct sum). Then if $P=\psi^{-1}\big(\varphi(O)\big)$ and is non-empty, $P$ can be given a manifold structure so that $(P,i)$ is a submanifold of $M$, where $i$ is the inclusion map, with

 $$ \dim M-\dim P=\dim N-\dim O. $$ 

Moreover, if $(O,\varphi)$ is an imbedded submanifold, then so is $(P,i)$, and in this case there is a unique manifold structure on $P$ such that $(P,i)$ is a submanifold of $M$.

In general, if $(O,\varphi)$ is not an imbedding, $P$ need not have the relative topology, and there is no unique manifold structure on $P$ such that $(P,i)$ is a submanifold. We leave it to the reader to supply examples.

PROOF The proof will consist of locally reducing this case to the case of Theorem 1.38. Let $p \in O$. By Proposition 1.35, we can pick a neighborhood $W$ of $p$ and a centered coordinate system $(V, \tau)$ with coordinate functions $x_{1}, \ldots, x_{d}$ about $\varphi(p)$ such that $\varphi(W)$ is the slice

(3)

 $$ x_{e+i}=0\qquad(j=1,\ldots,d-c). $$ 

Let

 $$ \pi\colon\mathbb{R}^{d}\to\mathbb{R}^{d-c}, $$ 

 $$ \pi(a)=(a_{e+1},\ldots,a_{d}). $$ 

So

(5)

 $$ \pi\circ\tau\bigl(\varphi(W)\bigr)=\{0\}. $$ 

Let

(6)

 $$ U=\psi^{-1}(V), $$ 

and let

(7)

 $$ \psi_{1}=\pi\circ\tau\circ\psi\mid U\colon U\to\mathbb{R}^{d-c}. $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//cfd2d4f8-2f72-4986-81e3-8d0f6ee731af/markdown_3/imgs/img_in_image_box_104_579_763_916.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A12Z%2F-1%2F%2F25d7888242b98ce45ec090bf36ac141e2d8b93edc291e380f453508340c4a286" alt="Image" width="67%" /></div>

Now, (3) through (7) imply that

 $$ \psi_{1}^{-1}(0)=\psi^{-1}\big(\varphi(W)\big). $$ 

For each point  $ m \in \psi_{1}^{-1}(0) $,  $ d\psi_{1} \mid M_{m} $ is surjective since  $ d(\pi \circ \tau) \mid N_{\psi(m)} $ is surjective and since by (1), (5), and (7)

 $$ d(\pi\circ\tau)(N_{\varphi(m)})=d\psi_{1}(M_{m})+\{0\}. $$ 

Thus by 1.38,  $ \psi^{-1}(\varphi(W)) $ has a unique manifold structure such that  $ (\psi^{-1}(\varphi(W)), i) $ is a submanifold of  $ M $; and in this manifold structure,

 $ \psi^{-1}\left(\varphi(W)\right) $ has the relative topology and has dimension equal to  $ \dim M - \dim N + \dim O $. Cover O by a countable collection  $ \{W_i: i = 1, 2, 3, \ldots\} $ of such sets. Then

 $$ P=\bigcup_{i=1}^{\infty}\psi^{-1}\bigl(\varphi(W_{i})\bigr). $$ 

If $i \neq j$, the submanifolds $\psi^{-1}(\varphi(W_i))$ and $\psi^{-1}(\varphi(W_i))$ intersect in open subsets of each other. It follows that the union of the topologies on the various $\psi^{-1}(\varphi(W_i))$ forms a basis for a topology on $P$. With this topology, $P$ is a locally Euclidean space with dimension equal to $\dim M - \dim N + \dim O$; and, moreover, $P$ is second countable since (9) expresses $P$ as a countable union of second countable open subsets. The manifold structures on the various $\psi^{-1}(\varphi(W_i))$ are compatible on overlaps because of the uniqueness of the manifold structure on $\psi^{-1}(\varphi(W_i))$ (or any open subset of $\psi^{-1}(\varphi(W_i))$) such that $(\psi^{-1}(\varphi(W_i)))$ is a submanifold of $M$ (by result (b) of 1.33). Thus the collection of coordinate systems on $P$ containing the coordinate systems on the various $\psi^{-1}(\varphi(W_i))$ and maximal with respect to 1.4(b) forms a differentiable structure on $P$. That $(P,i)$ is a submanifold of $M$ now follows immediately from the fact that the $(\psi^{-1}(\varphi(W_i)))$ are submanifolds. If $(O, \varphi)$ is an imbedding, the coordinate neighborhood $V$ can be chosen small enough so that $\varphi(O) \cap V$ consists only of the single slice $\varphi(W)$, and thus $U \cap P = \psi^{-1}(\varphi(W))$. It follows in this case that $P$ has the relative topology; hence $(P,i)$ is an imbedding. The uniqueness of the manifold structure in this case is guaranteed by result (b) of 1.33.

### 1.40 Examples

(a) The differential of the function $f(p) = \sum_{i=1}^{a} r_i(p)^2$ on $\mathbb{R}^d$ is surjective except at the origin. Thus it follows from 1.38 that the sphere $f^{-1}(r^2)$, for a constant $r > 0$, has a unique manifold structure for which it is a submanifold of $\mathbb{R}^d$ under the inclusion map. In particular, this is the same manifold structure as the one defined in Example 1.5(d).

(b) We define a map $\psi$ from the general linear group $Gl(d, \mathbb{R})$ (Example 1.5(f)) to the vector space of all real symmetric $d \times d$ matrices by

 $$ \psi(A)=A A^{t}, $$ 

where  $ A^{t} $ is the transpose of the matrix A. Let

 $$ O(d)=\psi^{-1}(I) $$ 

where $I$ is the $d \times d$ identity matrix. $O(d)$ is a subgroup of $Gl(d,\mathbb{R})$ under matrix multiplication called the orthogonal group. To apply 1.38 to conclude that $O(d)$ has a unique manifold structure such that $(O(d),i)$ is a submanifold of $Gl(d,\mathbb{R})$, and that in this manifold structure $i$ is an imbedding and $O(d)$ has dimension $\frac{1}{2}(d(d-1))$, one

need only check that  $ d\psi_\sigma $ is surjective at each  $ \sigma \in O(d) $. For this, it suffices to check that  $ d\psi_I $ is surjective, since whenever  $ \sigma \in O(d) $,

 $$ \varphi=\varphi\circ r_{o} $$ 

where  $ r_{\sigma} $ (right translation by  $ \sigma $) is the diffeomorphism of  $ Gl(d, \mathbb{R}) $ defined by  $ r_{\sigma}(\tau) = \tau\sigma $. We leave the details to the reader as an exercise.

##### VECTOR FIELDS

1.41 Definitions Smooth curves $\sigma: (a,b) \to M$ and their tangent vectors $\dot{\sigma}(t)$ were defined in 1.23(e). We say that a mapping $\sigma: [a,b] \to M$ is a smooth curve in $M$ if $\sigma$ extends to be a $C^\infty$ mapping of $(a-e, b+\varepsilon)$ into $M$ for some $\varepsilon > 0$. The curve $\sigma: [a,b] \to M$ is said to be piecewise smooth if there exists a partition $a = \alpha_0 < \alpha_1 < \cdots < \alpha_n = b$ such that $\sigma \mid [\alpha_t, \alpha_{t+1}]$ is smooth for each $t = 0, \ldots, n-1$. Observe that piecewise smooth curves are necessarily continuous. If $\sigma: [a,b] \to M$ is a smooth curve in $M$, then its tangent vector

 $$ \delta(t)=d\sigma\biggl(\frac{d}{d r}\biggl|_{t}\biggr)\in M_{\sigma(t)} $$ 

is well-defined for each  $ t \in [a, b] $.

1.42 Definitions A vector field X along a curve  $ \sigma $:  $ [a,b] \to M $ is a mapping  $ X\colon [a,b] \to T(M) $ which lifts  $ \sigma $; that is,  $ \pi \circ X = \sigma $. A vector field

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//39657b02-4b6c-4478-8c26-3631161b8894/markdown_1/imgs/img_in_image_box_133_752_767_1159.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A12Z%2F-1%2F%2Fc5b8ddebffbb41f1921c94691820368e7e191637890ed1428f39832a85e73a56" alt="Image" width="64%" /></div>

X is called a smooth $(C^{\infty})$ vector field along $\sigma$ if the mapping $X\colon[a,b]\to T(M)$ is $C^{\infty}$. A vector field $X$ on an open set $U$ in $M$ is a lifting of $U$ into $T(M)$, that is, a map $X\colon U\to T(M)$ such that

 $$ \pi\circ X=\mathrm{i d e n t i t y~m a p~o n~}U. $$ 

Again, for the vector field $X$ to be smooth ($C^\infty$) means that $X \in C^\infty(U, T(M))$. The set of smooth vector fields over $U$ forms in the obvious way a vector space over $\mathbb{R}$ and a module over the ring $C^\infty(U)$ of $C^\infty$ functions on $U$. If $X$ is a vector field on $U$ and $m \in U$, then $X(m)$ (often denoted $X_m$) is an element of $M_m$. If $f$ is a $C^\infty$ function on $U$, then $X(f)$ is the function on $U$ whose value at $m$ is $X_m(f)$.

1.43 Proposition Let X be a vector field on M. Then the following are equivalent:

(a) X is  $ C^{\infty} $.

(b) If $(U, x_{1}, \ldots, x_{d})$ is a coordinate system on $M$, and if $\{a_{i}\}$ is the collection of functions on $U$ defined by

 $$ X\mid U=\sum_{i=1}^{d}a_{i}\frac{\partial}{\partial x_{i}}, $$ 

then  $ a_{i} \in C^{\infty}(U) $.

(c) Whenever $V$ is open in $M$ and $f\in C^{\infty}(V)$, then $X(f)\in C^{\infty}(V)$.

PROOF (a) $\Rightarrow$ (b) The fact that $X$ is smooth implies that $X \mid U$ is smooth; and since the composition of differentiable maps is again differentiable, it follows that $dx_i \circ X \mid U$ is smooth. (Recall that the $dx_i$ are coordinate functions on $\pi^{-1}(U) \subset T(M)$, 1.25(3).) But

 $$ d x_{i}\circ X\mid U=a_{i}. $$ 

Hence the  $ a_{i} $ are  $ C^{\infty} $ functions on U.

(b) $\Rightarrow$ (c) It suffices to prove that $X(f) \mid U \in C^{\infty}(U)$ where $(U, x_{1}, \ldots, x_{d})$ is an arbitrary coordinate system on $M$ for which $U \subset V$. But, by (b),

 $$ X(f)\left|~U=\sum_{i=1}^{d}a_{i}\frac{\partial f}{\partial x_{i}},~\right. $$ 

and the right-hand side is a  $ C^{\infty} $ function on U.

(c) $\Rightarrow$ (a) To prove that $X$ is $C^{\infty}$, it suffices to prove that $X\mid U$ is $C^{\infty}$ where $(U, x_1, \ldots, x_d)$ is an arbitrary coordinate system on $M$. To prove that $X\mid U$ is $C^{\infty}$, we need only check that $X\mid U$ composed with the canonical coordinate functions $1.25(3)$ on $\pi^{-1}(U)$ are $C^{\infty}$ functions. Now, $x_i \circ \pi \circ X\mid U = x_i$ and $dx_i \circ X\mid U = X(x_i)$, all of which are $C^{\infty}$ functions on $U$.

1.44 Lie Bracket If X and Y are smooth vector fields on M, we define a vector field  $ [X,Y] $ called the Lie bracket of X and Y by setting

 $$ [X,Y]_{m}(f)=X_{m}(Y f)-Y_{m}(X f). $$ 

### 1.45 Proposition

(a) [X,Y] is indeed a smooth vector field on M.

(b) If $f, g \in C^{\infty}(M)$, then $[fX, gY] = fg[X, Y] + f(Xg)Y - g(Yf)X$.

(c)  $ [X,Y] = -[Y,X] $.

(d)  $ [[X,Y],Z] + [[Y,Z],X] + [[Z,X],Y] = 0 $ for all smooth vector fields X, Y, and Z on M.

We leave the proof as an exercise. Part (d) is known as the Jacobi identity. A vector space with a bilinear operation satisfying (c) and (d) is called a Lie algebra.

1.46 Definition Let $X$ be a smooth vector field on $M$. A smooth curve $\sigma$ in $M$ is an integral curve of $X$ if

 $$ \dot{\sigma}(t)=X(\sigma(t)) $$ 

for each t in the domain of  $ \sigma $.

1.47 Let $X$ be a $C^\infty$ vector field on $M$, and let $m \in M$. Let us now consider the question: Does there exist an integral curve of $X$ through $m$, and if so, is there a unique one?

A curve  $ \gamma $:  $ (a,b) \to M $ is an integral curve of X if and only if

 $$ d\gamma\left(\frac{d}{d r}\bigg|_{t}\right)=X\big(\gamma(t)\big)\qquad\big(t\in(a,b)\big). $$ 

Let us interpret this in coordinates. Suppose that  $ 0 \in (a,b) $ and  $ \gamma(0) = m $. Choose a coordinate system  $ (U,\varphi) $ with coordinate functions  $ x_1, \ldots, x_d $ about m. By 1.43(b),

 $$ X\mid U=\sum_{i=1}^{d}f_{i}\frac{\partial}{\partial x_{i}} $$ 

where the $f_{i}$ are $C^{\infty}$ functions on $U$. Moreover, for each $t$ such that $\gamma(t) \in U$,

 $$ d\gamma\left(\frac{d}{d r}\bigg\vert_{t}\right)=\sum_{i=1}^{d}\frac{d(x_{i}\circ\gamma)}{d r}\bigg\vert_{t}\frac{\partial}{\partial x_{i}}\bigg\vert_{r(t)}. $$ 

Thus, in view of (2) and (3), equation (1) becomes

 $$ \sum_{i=1}^{d}\frac{d(x_{i}\circ\gamma)}{d r}\bigg|_{t}\frac{\partial}{\partial x_{i}}\bigg|_{\gamma(t)}=\sum_{i=1}^{d}f_{i}(\gamma(t))\frac{\partial}{\partial x_{i}}\bigg|_{\gamma(t)}. $$ 

Thus $\gamma$ is an integral curve of $X$ on $\gamma^{-1}(U)$ if and only if

 $$ \left.\frac{d\gamma_{i}}{d r}\right|_{t}=f_{i}\circ\varphi^{-1}\big(\gamma_{1}(t),\ldots,\gamma_{d}(t)\big)\qquad\big(i=1,\ldots,d\quad\mathrm{a n d}\quad t\in\gamma^{-1}(U)\big), $$ 

where $\gamma_{t}=x_{t}\circ\gamma$. Equation (5) is a system of first order ordinary differential equations for which there exist fundamental existence and uniqueness theorems [11]. These theorems, when translated into manifold terminology, give the following.

1.48 Theorem Let $X$ be a $C^\infty$ vector field on a differentiable manifold $M$. For each $m\in M$ there exists $a(m)$ and $b(m)$ in $\mathbb{R}\cup\{\pm\infty\}$, and a smooth curve

(1)

 $$ \gamma_{m}\colon\big(a(m),b(m)\big)\to M $$ 

such that

(a)  $ 0 \in (a(m), b(m)) $ and  $ \gamma_m(0) = m $.

(b)  $ \gamma_{m} $ is an integral curve of X.

(c) If $\mu\colon(c,d)\to M$ is a smooth curve satisfying conditions (a) and (b), then $(c,d)\subset(a(m),b(m))$ and $\mu=\gamma_{m}\mid(c,d)$.

We continue with the statement of the theorem after the following.

Definition For each $t\in\mathbb{R}$, we define a transformation $X_{t}$ with domain

 $$ \mathcal{D}_{t}=\left\{m\in M\colon t\in\left(a(m),b(m)\right)\right\} $$ 

by setting

(3)

 $$ X_{t}(m)=\gamma_{m}(t). $$ 

(d) For each $m \in M$, there exists an open neighborhood $V$ of $m$ and $an \varepsilon > 0$ such that the map

(4)

 $$ (t,p)\mapsto X_{t}(p) $$ 

is defined and is  $ C^{\infty} $ from  $ (-\varepsilon,\varepsilon) \times V $ into M.

(e)  $ D_{t} $ is open for each t.

(f)  $ \bigcup \mathcal{D}_t = M $.

(g)  $ X_{t}\colon \mathcal{D}_{t} \to \mathcal{D}_{-t} $ is a diffeomorphism with inverse  $ X_{-t} $.

(h) Let $s$ and $t$ be real numbers. Then the domain of $X_{s} \circ X_{t}$ is contained in but generally not equal to $\mathcal{D}_{s+t}$. However, the domain of $X_{s} \circ X_{t}$ is $\mathcal{D}_{s+t}$ in the case in which $s$ and $t$ both have the same sign. Moreover, on the domain of $X_{s} \circ X_{t}$ we have

(5)

 $$ X_{s}\circ X_{t}=X_{s+t}. $$ 

PROOF We let $(a(m),b(m))$ be the union of all the open intervals which contain the origin and which are domains of integral curves of $X$ satisfying the initial condition that the origin maps to $m$. That $(a(m),b(m)) \neq \varnothing$ (and hence part (f) holds) follows from an application of the fundamental existence theorem [11, THEOREM 4, p. 28] to the system 1.47(5). Now if $\alpha$ and $\beta$ are integral curves of $X$ with domains the open intervals $A$ and $B$ (with $A \cap B \neq \varnothing$), and if $\alpha$ and $\beta$ have the same initial conditions $\alpha(t_0) = \beta(t_0)$ at some point $t_0 \in A \cap B$, then the subset of $A \cap B$ on which $\alpha$ and $\beta$ agree is nonempty, open by the basic uniqueness theorem [11, THEOREM 3, p. 28], and closed by continuity; and hence this subset is equal to $A \cap B$ by the connectedness of $A \cap B$. It follows that there exists a curve $\gamma_m$ defined on $(a(m), b(m))$ and satisfying parts (a), (b), and (c).

The existence of an $\varepsilon>0$ and a neighborhood $V$ of $m$ such that the map (4) is defined on $(-\varepsilon,\varepsilon)\times V$ is the content of THEOREM 7 on p. 29 of [11]. That the map (4) is smooth (and hence part (d) holds) follows from THEOREM 9 on p. 29 of [11] on the differentiability of the solutions of 1.47(5) with respect to their initial values.

Next we prove part (h). Let  $ t \in (a(m), b(m)) $. Then  $ s \mapsto \gamma_m(t + s) $ is an integral curve of X with the initial condition  $ 0 \mapsto \gamma_m(t) $ and with maximal domain  $ (a(m) - t, b(m) - t) $. It follows from part (c) that

 $$ (a(m)-t,b(m)-t)=\bigl(a\bigl(\gamma_{m}(t)\bigr),b\bigl(\gamma_{m}(t)\bigr)\bigr), $$ 

and for s in the interval (6),

 $$ \gamma_{\gamma_{m}(t)}(s)=\gamma_{m}(t+s). $$ 

Now let $m$ belong to the domain of $X_s \circ X_t$. Then $t \in (a(m), b(m))$ and $s \in (a(\gamma_m(t)), b(\gamma_m(t)))$, so by (6), $s + t \in (a(m), b(m))$. Thus $m \in \mathcal{D}_{s+t}$, and (5) follows from (7). It is easy to construct examples to show that the domain of $X_s \circ X_t$ is generally not equal to $\mathcal{D}_{s+t}$. (Consider, for example, the vector field $\partial/\partial r_1$ on $\mathbb{R}^3 - \{0\}$ with $s = -1$ and $t = 1$. If, however, $s$ and $t$ both have the same sign, and if $m \in \mathcal{D}_{s+t}$, that is, if $s + t \in (a(m), b(m))$, then it follows that $t \in (a(m), b(m))$ and, by (6), $s \in (a(\gamma_m(t)), b(\gamma_m(t)))$; hence $m$ is in the domain of $X_s \circ X_t$.

Parts (e) and (g) are trivial if $t=0$, so assume that $t>0$ and that $m\in\mathcal{D}_t$. (A similar argument will prove (e) and (g)) if $t<0$. It follows from part (d) and the compactness of $[0,t]$ that there exists a neighborhood $W$ of $\gamma_m([0,t]]$ and an $\varepsilon>0$ such that the map (4) is defined and $C^\infty$ on $(-\varepsilon,\varepsilon)\times W$. Choose a positive integer $n$ large enough so that $t/n\in(-\varepsilon,\varepsilon)$. Let $\alpha_1=X_{t/n}\mid W$, and let $W_1=\alpha_1^{-1}(W)$. Then for $i=2,\ldots,n$ we inductively define

 $$ \alpha_{i}=X_{t/n}\mid W_{t-1} $$ 

and

 $$ W_{t}=\alpha_{t}^{-1}(W_{t-1}). $$ 

$\alpha_{i}$ is a $C^{\infty}$ map on the open set $W_{t-1} \subset W$. It follows that $W_{n}$ is an open subset of $W$, that $W_{n}$ contains $m$ (since if $X_{t/n}$ composed with itself $n$ times is applied to $m$, we obtain $\gamma_{m}(t)$, which lies in $W$), and that by part (h),

 $$ \alpha_{1}\circ\alpha_{2}\circ\cdots\circ\alpha_{n}\mid W_{n}=X_{t}\mid W_{n}. $$ 

Consequently, $W_{n} \subset \mathcal{D}_{t}$; hence $\mathcal{D}_{t}$ is open, which proves part (e).

Finally, $X_{t}$ is a 1:1 map of $\mathcal{D}_{t}$ onto $\mathcal{D}_{-t}$ with inverse $X_{-t}$. That $X_{t}$ is $C^{\infty}$ (similarly for $X_{-t}$) follows from (8), which locally expresses $X_{t}$ as a composition of $C^{\infty}$ maps. Hence $X_{t}$ is a diffeomorphism from $\mathcal{D}_{t}$ to $\mathcal{D}_{-t}$, which proves part (g) and finishes Theorem 1.48.

1.49 Definitions A smooth vector field $X$ on $M$ is complete if $\mathcal{D}_t = M$ for all $t$ (that is, the domain of $\gamma_m$ is $(-\infty, \infty)$ for each $m \in M$). In this case, the transformations $X_t$ form a group of transformations of $M$ parametrized by the real numbers called the 1-parameter group of $X$. If $X$ is not complete, the transformations $X_t$ do not form a group since their domains depend on $t$. In this case, we shall refer to the collection of transformations $X_t$ as the local 1-parameter group of $X$.

1.50 Remarks A simple example of a non-complete vector field is obtained by considering the vector field $\partial/\partial r_{1}$ on the plane with the origin removed. If $a>0$, the domain of the maximal integral curve through $(a,0)$ is $(-a,+\infty)$. In the case in which the manifold $M$ is compact, any $C^{\infty}$ vector field on $M$ is complete. We leave the proof as an exercise.

1.51 Definition Let $\psi: M \to N$ be $C^\infty$. A smooth vector field $X$ along $\psi$ (that is, $X \in C^\infty(M, T(N))$ and $\pi \circ X = \psi$) has local $C^\infty$ extensions in $N$ if given $m \in M$ there exist a neighborhood $U$ of $m$ and a neighborhood $V$ of $\psi(m)$ such that $\psi(U) \subset V$, and there also exists a $C^\infty$ vector field $\tilde{X}$ on $V$ such that

 $$ \tilde{X}\circ\psi\mid U=X\mid U. $$ 

1.52 Remark It is easy to prove that a $C^{\infty}$ vector field $X$ along an immersion $\psi: M \to N$ always has local $C^{\infty}$ extensions in $N$. However, if $\psi$ is not an immersion, such extensions generally do not exist. Consider the following example. We shall first define a smooth vector field $X$ along a smooth curve $\alpha: \mathbb{R} \to \mathbb{R}$ in the real line. Let

 $$ \alpha(t)=t^{3}, $$ 

(that is,  $ \alpha = r^{3} $ where r is the canonical coordinate function on  $ \mathbb{R} $), and let

 $$ X(t)=\dot{\alpha}(t)=d\alpha\left(\frac{d}{d r}\bigg|_{t}\right). $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//209fd49e-d8af-44d0-93d5-311b55b43ae4/markdown_3/imgs/img_in_image_box_318_101_583_300.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2Ff489560058f2522ce56c7c0c9575b35b26713e7f94d3474be1a3368e9142be90" alt="Image" width="27%" /></div>

Since $\alpha$ is a homeomorphism, there is induced a vector field $\tilde{X}$ on $\mathbb{R}^{1}$ so that the above diagram commutes. Now, $X$ is a smooth vector field along $\alpha$, but $\tilde{X}$ is not a smooth vector field on $\mathbb{R}^{1}$. To show this, let $u = t^{3}$. Then

 $$ \begin{aligned}{\tilde{X}_{u}}&{{}=\tilde{X}_{\alpha(t)}=X(t)=d\alpha\bigg(\frac{d}{d r}\bigg|_{t}\bigg)}\\ {}&{{}=\frac{d\alpha}{d r}\bigg|_{t}\frac{d}{d r}\bigg|_{\alpha(t)}=3t^{2}\frac{d}{d r}\bigg|_{\alpha(t)}=3u^{2/3}\frac{d}{d r}\bigg|_{u}.}\\ \end{aligned} $$ 

Thus

 $$ \tilde{X}=3r^{2/3}\frac{d}{d r}, $$ 

and the function  $ r^{2/3} $ is not differentiable at the origin. If we extend  $ \alpha $ to be a mapping into the plane by setting

 $$ \alpha(t)=(t^{3},0), $$ 

and again we let $X(t)=\dot{\alpha}(t)$, then $X$ is a smooth vector field along the one-to-one $C^{\infty}$ curve $\alpha$ in the plane, which admits no local $C^{\infty}$ extension to a neighborhood of $(0,0)$.

1.53 Proposition Let $m \in M^{d}$, and let $X$ be a smooth vector field on $M$ such that $X(m) \neq 0$. Then there exists a coordinate system $(U, \varphi)$ with coordinate functions $x_{1}, \ldots, x_{d}$ on a neighborhood of $m$ such that

 $$ x\mid U=\frac{\partial}{\partial x_{1}}\mid U. $$ 

PROOF Choose a coordinate system $(V,\tau)$ centered at $m$ with coordinate functions $y_{1},\ldots,y_{d}$, such that

 $$ X_{m}=\frac{\partial}{\partial y_{1}}\Big|_{m}. $$ 

It follows from 1.48(d) that there exists an $\varepsilon>0$ and a neighborhood $W$ of the origin in $\mathbb{R}^{d-1}$ such that the map

 $$ \sigma(t,a_{2},\ldots,a_{d})=X_{t}\big(\tau^{-1}(0,a_{2},\ldots,a_{d})\big) $$ 

is well-defined and smooth for $(t, a_{2}, \ldots, a_{d}) \in (-\varepsilon, \varepsilon) \times W \subset \mathbb{R}^{d}$.

Now,  $ \sigma $ is non-singular at the origin since

 $$ d\sigma\bigg(\frac{\partial}{\partial r_{1}}\bigg|_{0}\bigg)=X_{m}=\frac{\partial}{\partial y_{1}}\bigg|_{m}\quad\mathrm{a n d}\quad d\sigma\bigg(\frac{\partial}{\partial r_{i}}\bigg|_{0}\bigg)=\frac{\partial}{\partial y_{i}}\bigg|_{m}\qquad(i\geq2). $$ 

Thus by Corollary (a) of 1.30,  $ \varphi = \sigma^{-1} $ is a coordinate map on some neighborhood U of m. Let  $ x_1, \ldots, x_d $ denote the coordinate functions of the coordinate system  $ (U, \varphi) $. Then since

 $$ d\sigma\bigg(\frac{\partial}{\partial r_{1}}\bigg|_{(t,a_{2},\ldots,a_{n})}\bigg)=X_{\sigma(t,a_{2},\ldots,a_{n})}\;, $$ 

we have

 $$ X\mid U=\frac{\partial}{\partial x_{1}}\mid U. $$ 

1.54 Definition Let  $ \varphi: M \to N $ be  $ C^\infty $. Smooth vector fields X on M and Y on N are called  $ \varphi $-related if  $ d\varphi \circ X = Y \circ \varphi $.

1.55 Proposition Let $\varphi: M \to N$ be $C^\infty$. Let $X$ and $X_1$ be smooth vector fields on $M$, and let $Y$ and $Y_1$ be smooth vector fields on $N$. If $X$ is $\varphi$-related to $Y$, and if $X_1$ is $\varphi$-related to $Y_1$, then $[X, X_1]$ is $\varphi$-related to $[Y, Y_1]$.

PROOF We must show that  $ d_{\phi} \circ [X, X_1] = [Y, Y_1] \circ \phi $. For this, let  $ m \in M $ and  $ f \in \dot{C}^{\infty}(N) $. Then we must show that

 $$ d_{\Phi}([X,X_{1}]_{m})(f)=[Y,Y_{1}]_{\varphi(m)}(f). $$ 

We simply unwind the definitions:

 $$ \begin{aligned}{d\varphi([X,X_{1}]_{m})(f)}&{{}=[X,X_{1}]_{m}(f\circ\varphi)}\\ {}&{{}=X_{m}\big(X_{1}(f\circ\varphi)\big)-X_{1}\big|_{m}\left(X(f\circ\varphi)\right)}\\ {}&{{}=X_{m}\big((d\varphi\circ X_{1})(f)\big)-X_{1}\big|_{m}\left((d\varphi\circ X)(f)\right)}\\ {}&{{}=X_{m}\big(Y_{1}(f)\circ\varphi\big)-X_{1}\big|_{m}\big(Y(f)\circ\varphi\big)}\\ {}&{{}=d\varphi(X_{m})\big(Y_{1}(f)\big)-d\varphi(X_{1}|_{m})\big(Y(f)\big)}\\ {}&{{}=Y_{\varphi(m)}\big(Y_{1}(f)\big)-Y_{1}\big|_{\varphi(m)}\left(Y(f)\right)}\\ {}&{{}=[Y,Y_{1}]_{\varphi(m)}(f).}\\ \end{aligned} $$ 

##### DISTRIBUTIONS AND THE FROBENIUS THEOREM

1.56 Definitions Let $c$ be an integer, $1 \leq c \leq d$. A $c$-dimensional distribution $\mathcal{D}$ on a $d$-dimensional manifold $M$ is a choice of a $c$-dimensional subspace $\mathcal{D}(m)$ of $M_m$ for each $m$ in $M$. $\mathcal{D}$ is smooth if for each $m$ in $M$ there is a neighborhood $U$ of $m$ and there are $c$ vector fields $X_1, \ldots, X_c$ of class $C^\infty$ on $U$ which span $\mathcal{D}$ at each point of $U$. A vector field $X$ on $M$ is said to belong to (or lie in) the distribution $\mathcal{D}(X \in \mathcal{D})$ if $X_m \in \mathcal{D}(m)$ for each

 $ m \in M $. A smooth distribution  $ \mathcal{D} $ is called involutive (or completely integrable) if  $ [X, Y] \in \mathcal{D} $ whenever  $ X $ and  $ Y $ are smooth vector fields lying in  $ \mathcal{D} $.

1.57 Definition A submanifold $(N,\psi)$ of $M$ is an integral manifold of a distribution $\mathcal{D}$ on $M$ if

 $$ d\varphi(N_{n})=\mathcal{D}\big(\psi(n)\big)\quad\mathrm{f o r~e a c h}n\in N. $$ 

1.58 Remarks Our object in this section is to prove that a necessary and sufficient condition for there to exist integral manifolds of $\mathcal{D}$ through each point of $M$ is that $\mathcal{D}$ be involutive. Perhaps a word of explanation is in order about the expression “completely integrable” sometimes used in place of “involutive.” We have required integral manifolds to be submanifolds whose tangent spaces coincide with the subspaces determined by the distribution. One could define a weaker notion of integral manifold by requiring only that the tangent spaces of the submanifold be contained in but not necessarily equal to the distribution at each point. It is possible for a distribution $\mathcal{D}$ to be “integrable” in the sense that it has low-dimensional “integral manifolds,” but not completely integrable in the sense that $\mathcal{D}$ does not have integral manifolds of the maximal dimension. For us, unless specified otherwise, integral manifolds of distributions will always be taken to mean integral manifolds of maximal dimension, that is, as defined in 1.57.

1.59 Proposition Let $\mathcal{D}$ be a smooth distribution on $M$ such that through each point of $M$ there passes an integral manifold of $\mathcal{D}$. Then $\mathcal{D}$ is involutive.

PROOF Let $X$ and $Y$ be smooth vector fields lying in $\mathcal{D}$, and let $m \in M$. We must prove that $[X, Y]_{m} \in \mathcal{D}(m)$. Let $(N, \psi)$ be an integral manifold of $\mathcal{D}$ through $m$, and suppose that $\psi(n_0) = m$. Since $d\psi: N_n \to \mathcal{D}(\psi(n))$ is an isomorphism at each $n$ in $N$, there exist vector fields $\widetilde{X}$, $\widetilde{Y}$ on $N$ such that

 $$ d\psi\circ\tilde{X}=X\circ\psi, $$ 

 $$ d\psi\circ\tilde{Y}=Y\circ\psi. $$ 

It is easily checked that $\tilde{X}$ and $\tilde{Y}$ are smooth. By 1.55, $[\tilde{X},\tilde{Y}]$ and $[X,Y]$ are $\psi$-related. Hence $[X,Y]_{m}=d\psi([\tilde{X},\tilde{Y}]_{n_{0}})\in\mathcal{D}(m)$.

1.60 Theorem (Frobenius) Let $\mathcal{D}$ be a $c$-dimensional, involutive, $C^{\infty}$ distribution on $M^{d}$. Let $m\in M$. Then there exists an integral manifold of $\mathcal{D}$ passing through $m$. Indeed, there exists a cubic coordinate system $(U,\varphi)$ which is centered at $m$, with coordinate functions $x_{1},\ldots,x_{d}$ such that the slices

 $$ x_{i}=\mathrm{c o n s t a n t}\qquad\mathrm{f o r~a l l~}i\in\{c+1,\ldots,d\} $$ 

are integral manifolds of $\mathcal{D}$; and if $(N,\psi)$ is a connected integral manifold of $\mathcal{D}$ such that $\psi(N)\subset U$, then $\psi(N)$ lies in one of these slices.

PROOF We shall prove the existence part of the theorem by induction on $c$. For the case $c=1$, choose a vector field $X$ lying in $\mathcal{D}$, defined on an open neighborhood of $m$, such that $X(m)\neq0$. Then Proposition 1.53 yields a coordinate system $(U,\varphi)$ about $m$, which can be taken to be cubic centered, for which $X\mid U=\partial/\partial x_1$. Hence the theorem holds for $c=1$.

Now assume that the theorem holds for $c-1$; we prove it for a distribution $\mathcal{D}$ of dimension $c$. Since $\mathcal{D}$ is smooth, there exist smooth vector fields $X_1,\ldots,X_c$ spanning $\mathcal{D}$ on a neighborhood $\tilde{V}$ of $m$. By 1.53, there exists a coordinate system $(V,y_1,\ldots,y_d)$ centered at $m$, with $V\subset\tilde{V}$, such that

 $$ X_{1}\mid V=\frac{\partial}{\partial y_{1}}. $$ 

On V, let

 $$ Y_{1}=X_{1}, $$ 

 $$ Y_{i}=X_{i}-X_{i}(y_{1})X_{1}\qquad(i=2,\ldots,c). $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//8a6047d9-2c8e-4af7-852e-1f5a884593c9/markdown_2/imgs/img_in_image_box_294_558_684_923.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A12Z%2F-1%2F%2F9351e3c936f95b36afc3bdd59dc8879cb30b8e2ae244c82a1b32ac9dec81f28c" alt="Image" width="41%" /></div>

Then the vector fields $Y_{1}, \ldots, Y_{e}$ are independent $C^{\infty}$ vector fields spanning $\mathcal{D}$ in $V$. Let $S$ be the slice $y_{1}=0$, and let

 $$ Z_{i}=Y_{i}\left|S\right.\quad(i=2,\ldots,c). $$ 

Then since (2) and (3) imply that

 $$ Y_{i}(y_{1})=0\qquad(i=2,\ldots,c), $$ 

the $Z_i$ are actually vector fields on $S$; that is, $Z_i(q) \in S_q$ whenever $q \in S$. The $Z_i$ span a smooth $c - 1$ dimensional distribution on $S$.

We claim this is involutive. Indeed, the $Z_{t}$ are $t$-related (inclusion map of $S$ in $M$) to the $Y_{t}$, and therefore, by 1.55, their Lie brackets are also $t$-related to the corresponding brackets of the $Y_{t}$. But $[Y_{t}, Y_{t}]$, $(i, j \geq 2)$, has no component in the $Y_{t}$ direction (apply to $y_{1}$ and get 0). Therefore, there exist $C^{\infty}$ functions $c_{ijk}$ such that

 $$ [Y_{i},Y_{j}]=\sum_{k=2}^{o}c_{i j k}Y_{k} $$ 

on V, and thus

 $$ [Z_{i},Z_{j}]=\sum_{k=2}^{e}c_{i j k}\bigg|_{S}Z_{k}. $$ 

This proves that the distribution on $S$ is involutive. By the induction hypothesis, there exists a centered coordinate system $w_{s}, \ldots, w_{d}$ on some neighborhood of $m$ in $S$ such that the slices defined by $w_{t} = \text{constant}$ for all $i \in \{c+1, \ldots, d\}$ are precisely the integral manifolds of the distribution spanned by $Z_{s}, \ldots, Z_{t}$ on this neighborhood.

The functions

 $$ \begin{aligned}{}&{{}x_{1}=y_{1},}\\ {}&{{}x_{j}=w_{j}\circ\pi\qquad(j=2,\ldots,d),}\\ \end{aligned} $$ 

where $\pi: V \to S$ is the natural projection in the $y$ coordinate system, are defined on some neighborhood of $m$ in $M$, are independent at $m$, and they all vanish at $m$. Thus there is a cubic-centered coordinate system $(U,\varphi)$ with the coordinate functions $x_{1},\ldots,x_{d}$ on a suitable neighborhood $U$ of $m$. We now prove that

 $$ Y_{t}(x_{o+r})\equiv0\quad\mathrm{o n}~U\qquad(i=1,\ldots,c;~r=1,\ldots,d-c). $$ 

From this it follows that the vector fields $\partial/\partial x_{1},\ldots,\partial/\partial x_{c}$ form a basis for $\mathcal{D}$ at each point of $U$, and thus the slices (1) are integral manifolds of $\mathcal{D}$.

To prove (9), first observe that (8) implies that

 $$ \frac{\partial x_{j}}{\partial y_{1}}=\left\{\begin{aligned}{}&{{}1\quad}&{(j=1)}\\ {}&{{}0\quad}&{(j=2,\ldots,d)}\\ \end{aligned}\right. $$ 

on $U$; and thus (2), (3), and (10) imply that

 $$ Y_{1}=\frac{\partial}{\partial x_{1}}\mathrm{\quad on~}U, $$ 

so certainly (9) holds for $i = 1$. Now let $i \in \{2, \ldots, c\}$ and $r \in \{1, \ldots, d - c\}$. By (11),

 $$ \frac{\partial}{\partial x_{1}}\left(Y_{i}(x_{c+r})\right)=Y_{1}\big(Y_{i}(x_{c+r})\big)=[Y_{1},Y_{i}](x_{c+r}). $$ 

The involutivity of $\mathcal{D}$ implies that there are $C^{\infty}$ functions $c_{ik}$ such that

 $$ [Y_{1},Y_{i}]=\sum_{k=1}^{e}c_{i k}Y_{k}. $$ 

Using (13), (12) becomes

 $$ \frac{\partial}{\partial x_{1}}\left(Y_{i}(x_{e+r})\right)=\sum_{k=2}^{e}c_{i k}Y_{k}(x_{e+r})\quad(i=2,\ldots,c;r=1,\ldots,d-c). $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//c4b76db3-fcb4-479b-8e7a-02a05f323e35/markdown_0/imgs/img_in_image_box_173_247_798_592.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A11Z%2F-1%2F%2F7fa55d5e100a1bdc333866b58c24afff47937358d18fb3c17fb7700abb9001ef" alt="Image" width="65%" /></div>

Fix a slice of $U$ of the form $x_{2}=$ constant, ..., $x_{d}=$ constant. On such a slice, $Y_{t}(x_{e+r})$ is a function of $x_{1}$ alone, and (14) becomes a system of $c-1$ homogeneous linear differential equations with respect to $x_{1}$. Such a system has a unique solution with given initial values [11]. Since the system is homogeneous, the 0 functions give a solution. But each such slice has a unique point in $S\cap U$, and on $S\cap U$,

 $$ Y_{i}(x_{c+r})=Z_{i}(w_{c+r})=0\qquad(i=2,\ldots,c). $$ 

The first equality follows from (4) and (8), and the second from the fact that the integral manifolds of the distribution on $S$ determined by the $Z_{t}$ are given by suitable slices in the $w$ coordinate system. It follows from (14) and (15) that the functions $Y_{t}(x_{e+r})$ must be identically zero on $U$. Thus (9) holds, and the induction step is completed.

Finally, suppose that $(N,\psi)$ is a connected integral manifold of $\mathcal{D}$ such that $\psi(N)\subset U$. Let $\pi$ be the projection of $\mathbb{R}^d$ onto the last $d-c$ coordinates. Then vectors in $\mathcal{D}$ are annihilated by $d(\pi\circ\varphi)$. Thus

 $$ d(\pi\circ\varphi\circ\psi)|_{n}\equiv0 $$ 

for each $n \in N$. By $1.24$, $\pi \circ \varphi \circ \psi$ is a constant map since $N$ is connected. Thus $\psi(N)$ is contained in one of the slices (1).

1.61 Remarks The classical version of the Frobenius theorem appears quite different from our version in 1.60. The classical Frobenius theorem can be formulated as follows.

Let $U$ and $V$ be open sets in $\mathbb{R}^m$ and $\mathbb{R}^n$ respectively. We use coordinates $r_1, \ldots, r_m$ on $\mathbb{R}^m$ and $s_1, \ldots, s_n$ on $\mathbb{R}^n$. Let

 $$ b\colon U\times V\to M(n,m) $$ 

be a $C^{\infty}$ map of $U\times V$ into the set of all $n\times m$ real matrices, and let $(r_{0},s_{0})\in U\times V$. If

 $$ \begin{array}{r l r}&{}&{\frac{\partial b_{i\beta}}{\partial r_{\gamma}}-\frac{\partial b_{i\gamma}}{\partial r_{\beta}}+\displaystyle\sum_{s=1}^{n}\left(\frac{\partial b_{i\beta}}{\partial s_{s}}\;b_{i\gamma}-\frac{\partial b_{i\gamma}}{\partial s_{j}}\;b_{j\beta}\right)=0}\\ &{}&{(i=1,\ldots,n;\gamma,\beta=1,\ldots,m)}\end{array} $$ 

on $U\times V$, then there exist neighborhoods $U_{\theta}$ of $r_{\theta}$ in $U$ and $V_{\theta}$ of $s_{\theta}$ in $V$ and a unique $C^{\infty}$ map

 $$ \alpha\colon U_{\mathfrak{g}}\times V_{\mathfrak{g}}\to V $$ 

such that if

 $$ \alpha_{s}(r)=\alpha(r,s)\qquad(s\in V_{0},\quad r\in U_{0}), $$ 

then

 $$ \alpha_{s}(r_{0})=s, $$ 

 $$ d\alpha_{s}|_{r}=b(r,\alpha(r,s)) $$ 

for all  $ (r,s)\in U_{0}\times V_{0} $

Equation (4) is a so-called total differential equation. We specify in (1) what the differential of a map should be as a function of the graph, and in (2) we have a necessary and sufficient condition for the existence of such a map with the specified initial conditions. It can be shown that this version is equivalent to 1.60. For example, if we start with a c-dimensional, involutive,  $ C^\infty $ distribution  $ \mathcal{D} $ on  $ M^d $ and a point  $ m \in M $, then we can obtain 1.60 from the classical version as follows. We can first choose a coordinate system  $ (W, \tau) $ about  $ m $ with coordinate functions  $ y_1, \ldots, y_d $ and with  $ \tau(W) = U \times V \subset \mathbb{R}^e \times \mathbb{R}^{d-e} $, for which there exist  $ C^\infty $ functions  $ f_{ji} $ on  $ U \times V $ ( $ i = 1, \ldots, c $;  $ j = 1, \ldots, d-c $) such that the vector fields

 $$ Y_{i}=\frac{\partial}{\partial y_{i}}+\sum_{i=1}^{d-c}f_{ji}\circ\tau\frac{\partial}{\partial y_{e+j}}\qquad(i=1,\ldots,c) $$ 

span D on W. Then we define a map b as in (1) by setting

 $$ b(r,s)=\{f_{j i}(r,s)\}. $$ 

It turns out that the involutivity of $\mathcal{D}$ implies that (2) is satisfied, and from the map $\alpha$ one can obtain the desired coordinate system 1.60(1). Conversely, one can obtain the classical version from 1.60 in a similar way.

We shall give in Chapter 2 yet another version of the Frobenius theorem in terms of differential forms and differential ideals.

In 1.32 we considered the situation in which a $C^{\infty}$ map $\psi: N \to M$ factors through a submanifold $(P,\varphi)$ of $M$ so that $\psi = \varphi \circ \psi_{\oplus}$ where $\psi_{\oplus}: N \to P$, and we sought sufficient conditions for $\psi_{\oplus}$ to be $C^{\infty}$. An important case occurs when $(P,\varphi)$ is an integral manifold of an involutive distribution on $M$.

1.62 Theorem Suppose that $\psi: N \to M^d$ is $C^\infty$, that $(P^c, \varphi)$ is an integral manifold of an involutive distribution $\mathcal{D}$ on $M$, and that $\psi$ factors through $(P, \varphi)$, that is, $\psi(N) \subset \varphi(P)$. Let $\psi_0: N \to P$ be the (unique) mapping such that $\varphi \circ \psi_0 = \psi$.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//c4b76db3-fcb4-479b-8e7a-02a05f323e35/markdown_2/imgs/img_in_image_box_351_351_552_477.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A12Z%2F-1%2F%2F65bce4e560e27b07ba07deebe0a3a442f5f309f4f25091b1d0abc750928ea533" alt="Image" width="21%" /></div>

Then  $ \psi_{0} $ is continuous (and hence  $ C^{\infty} $ by 1.32(a)).

PROOF Let $p$ belong to an open set $U$ in $P$, and let $n\in\psi_0^{-1}(p)$. Using 1.60, we can obtain an open set $\tilde{U}$ with $p\in\tilde{U}\subset U$ and a cubic coordinate system $(V,\tau)$ centered at $\varphi(p)$ with coordinate functions $x_1,\ldots,x_d$ such that the slices

 $$ x_{i}=\mathrm{c o n s t a n t}\qquad\mathrm{f o r~a l l~}i\in\{c+1,\ldots,d\} $$ 

are the integral manifolds of $\mathscr{D}$ in $V$, and such that $\varphi(U)$ is the slice

 $$ x_{c+1}=\cdots=x_{d}=0. $$ 

$\psi^{-1}(V)$ is open in $N$. Let $W$ be the component of $\psi^{-1}(V)$ containing $n$. $W$ is open. To prove that $\psi_0$ is continuous, we need only prove that $\psi_0(W) \subset \tilde{U} \subset U$. By the commutativity of (1) and the injectivity of $\psi$, it suffices to prove that $\psi(W)$ lies in the slice (3) of $V$. Now, $\psi$ is continuous and $W$ connected; hence $\psi(W)$ is connected. Moreover, $\psi(W)$ has at least the point $\psi(n)$ in common with the slice (3). So since $\psi(W)$ lies in a component of $\varphi(P) \cap V$, it is sufficient to prove that components of $\varphi(P) \cap V$ are contained in slices of the form (2).

Let $C$ be a component of $\varphi(P) \cap V$, and let $\pi: V \to \mathbb{R}^{d-c}$ be defined by

 $$ \pi(m)=\left(x_{c+1}(m),\ldots,x_{d}(m)\right). $$ 

Then since $P$ is second countable, and since $\varphi(P) \cap V$ is a union of the slices (2) due to the fact that $(P,\varphi)$ is an integral manifold of $\mathcal{D}$, it follows that $\pi(\varphi(P) \cap V)$ consists of a countable number of points in $\mathbb{R}^{d-c}$. Thus $\pi(C)$ is a connected countable subset of $\mathbb{R}^{d-c}$; hence $\pi(C)$ is a single point, and $C$ lies in a single slice.

1.63 Definition A maximal integral manifold $(N,\psi)$ of a distribution $\mathcal{D}$ on a manifold $M$ is a connected integral manifold of $\mathcal{D}$ whose image in $M$ is not a proper subset of any other connected integral manifold of $\mathcal{D}$. That is, there does not exist a connected integral manifold $(N_1,\psi_1)$ of $\mathcal{D}$ such that $\psi(N)$ is a proper subset of $\psi_1(N_1)$.

1.64 Theorem Let $\mathcal{D}$ be a $c$-dimensional, involutive, $C^{\infty}$ distribution on $M^{d}$. Let $m \in M$. Then through $m$ there passes a unique maximal connected integral manifold of $\mathcal{D}$, and every connected integral manifold of $\mathcal{D}$ through $m$ is contained in the maximal one.

PROOF Existence Let K be the set of all those points p in M for which there is a piecewise smooth curve joining m to p whose smooth portions

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//c4b76db3-fcb4-479b-8e7a-02a05f323e35/markdown_3/imgs/img_in_image_box_316_422_604_490.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A13Z%2F-1%2F%2Ff390b5a99b89a892ecc325ff1c0b1eb007a94e54e216ea7357f5937ecc6cadea" alt="Image" width="29%" /></div>

<div style="text-align: center;"><div style="text-align: center;">Integral curve of 2</div> </div>

are 1-dimensional integral curves of $\mathcal{D}$, that is, their tangent vectors belong to $\mathcal{D}$. By 1.60 and the second countability of $M$, there is a countable covering of $M$ by cubic coordinate systems $\{(U_{t}, x_{1}^{t}, \ldots, x_{d}^{t}) : i = 0, 1, 2, \ldots\}$ such that the integral manifolds of $\mathcal{D}$ in $U_{t}$ are the slices

 $$ x_{c+s}^{i}=\mathrm{c o n s t a n t}\qquad\mathrm{f o r~a l l~}j\in\{1,\ldots,d-c\}. $$ 

We shall assume that  $ m \in U_{0} $

Now let $p \in K$. Then there exists an index $i$, such that $p \in U_{i_p}$, and there is a slice $S_{i_p}$ of $U_{i_p}$ of the form (1) containing $p$. Observe that $S_{i_p} \subset K$. It follows from 1.60 that the collection of all open subsets of all such $S_{i_p}$ as $p$ runs over $K$ forms a basis for a locally Euclidean topology on $K$, and that we obtain a differentiable structure on $K$ if we take the maximal family of coordinate systems (with respect to 1.4(b)) containing the collection

 $$ \{(S_{i_{p}},\;x_{1}^{i_{p}}\;\big|\;S_{i_{p}},\;\ldots,\;x_{c}^{i_{p}}\;\big|\;S_{i_{p}}):p\in K\}. $$ 

We claim that $K$ with this topology and differentiable structure is a connected differentiable manifold of dimension $c$. $K$ is clearly connected since it is pathwise connected by construction. We have only to prove that the topology on $K$ is second countable. For this, fix an $i\in(0,1,2,\ldots)$. We need only show that there are at most countably many slices of $U_{i}$ in $K$. Each point of $U_{i}$ which lies in $K$ is joinable to $m$ by a piecewise smooth curve whose range also lies in $K$. To each such curve from $m$ to points in $U_{i}$ there corresponds (although not uniquely) a finite sequence

 $$ U_{0},~U_{i_{1}},~\ldots,~U_{i_{n}},~U_{i} $$ 

of the coordinate neighborhoods through which the curve passes in order. The curve thus begins in the slice of U_{t_{0}} containing m, passes through some slice of U_{t_{1}}, then through some slice of U_{t_{2}}, and so on, until in a finite number of steps it reaches a slice in U_{t}. Since there are at most countably many such sequences (3) from U_{t} to U_{t_{1}}, we need only show that for each such sequence there are at most countably many slices of U_{t} reachable in the above manner.  $ \underline{\text{For this,}} $ we need only observe that for any j, k \in (0, 1, \ldots) a single slice of U_{t} can intersect at most countably many slices of U_{k}; for if S is a slice of U_{t_{1}}, then S \cap U_{k} is an open submanifold of S and therefore consists of at most countably many components, each such component being a connected integral manifold of \mathcal{D} in U_{k}, and hence lying in a slice of U_{k}. This proves the second countability of K.

 $ (K,i) $, where  $ i: K \to M $ is the inclusion map, is now a submanifold of  $ M $ and is a connected integral manifold of  $ \mathcal{D} $ passing through  $ m $. Moreover,  $ (K,i) $ is a maximal connected integral manifold of  $ \mathcal{D} $. For let  $ (N,\psi) $ be any connected integral manifold of  $ \mathcal{D} $ passing through  $ m $, and let  $ p \in \psi(N) $. There is a piecewise smooth curve  $ c: [0,1] \to N $ joining  $ \psi^{-1}(m) $ to  $ \psi^{-1}(p) $. (Connected manifolds are pathwise connected.) Then  $ \psi \circ c $ is a piecewise smooth 1-dimensional integral curve of  $ \mathcal{D} $ connecting  $ m $ to  $ p $. Thus  $ p \in K $, and so  $ \psi(N) \subset K $, which proves that  $ K $ is maximal. Thus we have proved the existence of a maximal connected integral manifold  $ (K,i) $ of  $ \mathcal{D} $ passing through  $ m $, and have proved that every connected integral manifold of  $ \mathcal{D} $ through  $ m $ has its image in  $ K $.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//3d509304-d411-4786-813d-cdca1c258207/markdown_0/imgs/img_in_image_box_503_282_816_506.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A12Z%2F-1%2F%2F39c7dd790effcbe5e0ec067865cf2356e1b0b1c32811c437f9a91c4b44525f38" alt="Image" width="32%" /></div>

Uniqueness (cf. 1.33) Let $(N,\psi)$ be any other maximal connected integral manifold of $\mathcal{D}$ passing through $m$. As we have observed above, $\psi(N) \subset K$; thus $\psi$ factors as follows:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//3d509304-d411-4786-813d-cdca1c258207/markdown_0/imgs/img_in_image_box_336_889_529_1014.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A12Z%2F-1%2F%2Fdd7273880c8ad5e48826cb17e4963bbfe9213877438dae6c14876bf890b2c49d" alt="Image" width="20%" /></div>

$\psi_{0}$ is $C^{\infty}$ by 1.62, and is 1:1 and non-singular since $\psi$ is 1:1 and non-singular. $\psi_{0}$ is onto since the fact that $(N,\psi)$ is a maximal integral manifold of $\mathcal{D}$ through $m$ implies that $\psi(N)$ cannot be a proper subset of $K$. It follows from Corollary (a) of 1.30 that $\psi_{0}$ is a diffeomorphism. Thus $(N,\psi)$ and $(K,i)$ are equivalent, and the maximal connected integral manifold of $\mathcal{D}$ through $m$ is unique.

##### EXERCISES

1 Prove that in Example 1.5(d) one does indeed obtain a differentiable structure on  $ S^{d} $.

2 The usual differentiable structure on the real line $\mathbb{R}$ was obtained by taking $\mathcal{F}$ to be the maximal collection containing the identity map. Let $\mathcal{F}_1$ be the maximal collection (with respect to $1.4(b)$ containing the map $t \mapsto t^2$. Prove that $\mathcal{F} \neq \mathcal{F}_1$, but that $(\mathbb{R},\mathcal{F})$ and $(\mathbb{R},\mathcal{F}_1)$ are diffeomorphic.

3 Let $\{U_{\alpha}\}$ be an open cover of a manifold $M$. Prove that there exists a refinement $\{V_{\alpha}\}$ such that $\overline{V}_{\alpha} \subset U_{\alpha}$ for each $\alpha$.

4 Use the fact that manifolds are regular and paracompact to prove that manifolds are normal topological spaces.

5 Prove 1.25(a), (b), and (c).

6 Prove that if $\psi: M \to N$ is $C^{\infty}$, one-to-one, onto, and everywhere non-singular, then $\psi$ is a diffeomorphism. (This proposition depends strongly on the second countability of $M$. Here is an outline for a proof. This map $\psi$ is a diffeomorphism if and only if $d\psi$ is surjective everywhere. If $d\psi$ is not surjective at some point, then the dimension of $M$ is less than the dimension of $N$. Let $\dim M = p$ and $\dim N = d$. Assuming that $p < d$, one arrives at a contradiction as follows. Let $(U,\varphi)$ be a coordinate system on $N$ such that $\varphi(U) = \mathbb{R}^d$. Since $\psi$ maps $M$ onto $N$, the range of $\varphi \circ \psi$ is all of $\mathbb{R}^d$. Now we show that this yields a contradiction. One way is to use 1.35 to observe that the range of $\varphi \circ \psi$ is a countable union of nowhere dense sets in $\mathbb{R}^d$, and therefore, by the Baire category theorem, could not possibly be all of $\mathbb{R}^d$. Another way is to use the fact that $p < d$ to prove that the range of $\varphi \circ \psi$ has measure 0 in $\mathbb{R}^d$, which also is a contradiction (where a set in $\mathbb{R}^d$ has measure 0 if it can be covered by a sequence of balls, the union of whose volumes is arbitrarily small). That the range of $\varphi \circ \psi$ has measure 0 in $\mathbb{R}^d$ follows from the second countability of $M$ and the fact that a $C^1$ map $\mathbb{R}^d \to \mathbb{R}^d$ has image of measure 0, and this, in turn, follows from the fact that a $C^1$ map $\mathbb{R}^d \to \mathbb{R}^d$ takes sets of measure 0 to sets of measure 0. To prove the latter, observe that if $f: \mathbb{R}^d \to \mathbb{R}^d$ is $C^1$, and if $A$ is a compact set in $\mathbb{R}^d$, then $f$ has a Lipschitz constant $K$ on $A$,

 $$ \|f(x)-f(y)\|\leq K\|x-y\|\quad(x,y\in A), $$ 

so that $f$ magnifies the volume of balls in $A$ by at most $K^{d}$, and hence takes sets of measure 0 in $A$ into sets of measure 0.)

7 Prove 1.33(a) and (b).

8 Obtain the classical implicit function theorem 1.37 from 1.38.

9 Let  $ f\colon \mathbb{R}^2 \to \mathbb{R} $ be defined by.

 $$ f(x,y)=x^{3}+x y+y^{3}+1. $$ 

For which points $p = (0,0)$, $p = (\tfrac{1}{3},\tfrac{1}{3})$, $p = (-\tfrac{1}{3},-\tfrac{1}{3})$ is $f^{-1}(f(p))$ an imbedded submanifold in $\mathbb{R}^2$?

10 Let $M$ be a compact manifold of dimension $n$, and let $f: M \to \mathbb{R}^n$ be $C^\infty$. Prove that $f$ cannot everywhere be non-singular.

11 Find counterexamples to show that Proposition 1.36 would fail if either of the hypotheses closed or imbedded were deleted. In fact, one can prove more; namely, if $(M,\psi)$ is a submanifold of $N$ such that whenever $g\in C^\infty(M)$ there is a $C^\infty$ function $f$ on $N$ such that $f\circ\psi=g$, then $\psi$ is an imbedding and $\psi(M)$ is closed in $N$.

12 Supply the details for 1.40(a) and (b).

13 Prove Proposition 1.45.

14 Is every vector field on the real line complete?

15 Prove that if $(U, x_1, \ldots, x_d)$ is a coordinate system on $M$, then $[\partial/\partial x_i, \partial/\partial x_j] = 0$ on $U$.

16 Let $N \subset M$ be a submanifold. Let $\gamma: (a,b) \to M$ be a $C^\infty$ curve such that $\gamma(a,b) \subset N$. Show that it is not necessarily true that $\dot{\gamma}(t) \in N_{\gamma(t)}$ for each $t \in (a,b)$.

17 Prove that any $C^{\infty}$ vector field on a compact manifold is complete.

18 Prove that a $C^{\infty}$ map $f\colon \mathbb{R}^{8} \to \mathbb{R}^{1}$ cannot be one-to-one.

19 Supply the details of the equivalence of the two versions 1.60 and 1.61 of the Frobenius theorem.

20 Let $\varphi: N \to M$ be $C^\infty$, and let $X$ be a $C^\infty$ vector field on $N$. Suppose that $d\varphi(X(p)) = d\varphi(X(q))$ whenever $\varphi(p) = \varphi(q)$. Is there a smooth vector field $Y$ on $M$ which is $\varphi$-related to $X?$

21 The torus is the manifold $S^{1} \times S^{1}$. Consider $S^{1}$ as the unit circle in the complex plane. We define a mapping $\varphi: \mathbb{R} \to S^{1} \times S^{1}$ by setting $\varphi(t) = (e^{\mathfrak{z}_{\pi i t}}, e^{\mathfrak{z}_{\pi i a t}})$ where $\alpha$ is an irrational number. Prove that $(\mathbb{R}, \varphi)$ is a dense submanifold of $S^{1} \times S^{1}$. This submanifold is known as the skew line on the torus.

22 Let $\gamma(t)$ be an integral curve of a vector field $X$ on $M$. Suppose that $\dot{\gamma}(t)=0$ for some $t$. Prove that $\gamma$ is a constant map, that is, its range consists of one point.

23 A Riemannian structure on a differentiable manifold M is a smooth choice of a positive definite inner product  $ \langle\cdot,\rangle_{m} $ on each tangent space  $ M_{m} $, smooth in the sense that whenever X and Y are  $ C^{\infty} $ vector fields on M, then  $ \langle X,Y\rangle $ is a  $ C^{\infty} $ function on M. Prove that there exists a Riemannian structure on every differentiable manifold. You will need to use a partition of unity argument. A Riemannian manifold is a differentiable manifold together with a Riemannian structure.

24 Consider the product manifold  $ M \times N $ with the canonical projections  $ \pi_1: M \times N \to M $ and  $ \pi_8: M \times N \to N $.

(a) Prove that  $ \alpha\colon \tilde{M} \to M \times N $ is  $ C^\infty $ if and only if  $ \pi_1 \circ \alpha $ and  $ \pi_2 \circ \alpha $ are  $ C^\infty $.

(b) Prove that the map $v \mapsto (d\pi_{1}(v), d\pi_{2}(v))$ is an isomorphism of $(M \times N)_{(m,n)}$ with $M_{m} \oplus N_{n}$.

(c) Let $X$ and $Y$ be $C^{\infty}$ vector fields on $M$ and $N$ respectively. Then, by (b), $X$ and $Y$ canonically determine vector fields $\tilde{X} = (X,0)$ and $\tilde{Y} = (0,Y)$ on $M \times N$. Prove that $[X, \tilde{Y}] = 0$.

(d) Let  $ (m_{0}, n_{0}) \in M \times N $, and define injections  $ i_{n_{0}}: M \to M \times N $ and  $ i_{m_{0}}: N \to M \times N $ by setting

 $$ \begin{aligned}{}&{{}i_{n_{0}}(m)=(m,n_{0}),}\\ {}&{{}i_{m_{0}}(n)=(m_{0},n).}\\ \end{aligned} $$ 

Let  $ v \in (M \times N)_{(m_0, n_0)} $, and let  $ v_1 = d\pi_1(v) \in M_{m_0} $ and  $ v_2 = d\pi_2(v) \in N_{m_0} $. Let  $ f \in C^\infty(M \times N) $. Prove that

 $$ v(f)=v_{1}(f\circ i_{n_{0}})+v_{1}(f\circ i_{m_{0}}). $$
