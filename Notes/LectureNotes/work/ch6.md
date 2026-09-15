THE HODGE THEOREM

Throughout this chapter, $M$ will be a compact oriented Riemannian manifold of dimension $n$ unless otherwise indicated. We will see that the ordinary Laplacian $(-1)\sum_{i}\partial^{2}/\partial x_{i}^{2}$ has a generalization to an operator $\Delta$ on differential forms, known as the Laplace-Beltrami operator. Our main objective in this chapter is a proof of the Hodge decomposition theorem, which says that the equation $\Delta\omega=\alpha$ has a solution $\omega$ in the smooth $p$-forms on $M$ if and only if the $p$-form $\alpha$ is orthogonal (in a suitable inner product on $E^{p}(M)$ to the space of harmonic $p$-forms (those for which $\Delta\varphi=0$). From the Hodge decomposition theorem we will conclude that there exists a unique harmonic form in each of Rham cohomology class. As another simple application we will obtain the Poincaré duality theorem for de Rham cohomology and, from it, the Poincaré duality theorem for real singular cohomology. To prove the Hodge theorem, we shall give a complete self-contained exposition of the local theory of elliptic operators, using Fourier series as our basic tool. The eigenfunctions of the Laplace-Beltrami operator and their use in a proof of the Peter-Weyl theorem are discussed in the exercises at the end of this chapter.

##### THE LAPLACE-BELTRAMI OPERATOR

6.1 Definitions Recall (from 4.10(6) and Exercise 13 of Chapter 2) that there is a linear operator * which assigns to each p-form on M an  $ (n-p) $ form and which satisfies

 $$ **=(-1)^{p(n-p)}. $$ 

We define an operator $\delta$ from $p$-forms to $(p-1)$ forms by setting

 $$ \delta=(-1)^{n(p+1)+1}{*}d{*}. $$ 

On 0-forms, $\delta$ is simply the zero linear functional. The Laplace-Beltrami operator $\Delta$ (Laplacian for short) is defined by

 $$ \Delta=\delta d+d\delta, $$ 

and is a linear operator on  $ E^p(M) $ for each  $ p $ with  $ 0 \leq p \leq n $. We leave it 220

to the reader as an exercise to check that on $E^{0}(\mathbb{R}^{n})$, that is, on $C^{\infty}$ functions on Euclidean space $\mathbb{R}^{n}$, the Laplacian is simply the operator $(-1)\sum_{i=1}^{n}\partial^{2}/\partial x_{i}^{2}$. Also, it is a straightforward exercise to check that the Laplacian commutes with *, that is,

 $$ *\triangle=\triangle*. $$ 

We define an inner product on the vector space $E^{p}(M)$ of $p$-forms on $M$ by setting

 $$ \langle\alpha,\beta\rangle=\int_{M}\alpha\wedge\ast\beta\quad\mathrm{f o r}\alpha,\beta\in E^{d}(M), $$ 

and we denote the corresponding norm by  $ \|\alpha\| $. It follows from (6) of Exercise 13 in Chapter 2 that the bilinear form defined in (5) is actually symmetric and positive definite. We extend the inner products (5) for  $ 0 \leq p \leq n $ to an inner product on the direct sum  $ \sum_{p=0}^{n} E^p(M) $ simply by requiring the various  $ E^p(M) $ to be orthogonal.

6.2 Proposition $\delta$ is the adjoint of $d$ on $\sum_{p=0}^{n} E^{p}(M)$; that is,

(1)

 $$ \langle d\alpha,\beta\rangle=\langle\alpha,\delta\beta\rangle. $$ 

PROOF By linearity, and the orthogonality of the $E^{p}(M)$, the proof reduces to consideration of the case in which $\alpha$ is a $(p-1)$ form and $\beta$ is a $p$-form. In this case,

 $$ \begin{aligned}{d(\alpha\wedge{*}\beta)}&{{}=d\alpha\wedge{*}\beta+(-1)^{*-1}\alpha\wedge d{*}\beta}\\ {}&{{}=d\alpha\wedge{*}\beta-\alpha\wedge{*}\delta\beta.}\\ \end{aligned} $$ 

By integrating both sides over $M$ and applying the special case of Stokes' theorem contained in the corollary of 4.9 to the left-hand side, we obtain

(3)

 $$ 0=\int_{\mathcal{M}}(d\alpha\wedge*\beta-\alpha\wedge*\delta\beta)=\langle d\alpha,\beta\rangle-\langle\alpha,\delta\beta\rangle. $$ 

Thus

(4)

 $$ \langle d\alpha,\beta\rangle=\langle\alpha,\delta\beta\rangle. $$ 

Corollary  $ \Delta $ is self-adjoint, that is,

 $$ \langle\Delta\alpha,\beta\rangle=\langle\alpha,\Delta\beta\rangle\qquad(\alpha,\:\beta\in E^{\mathfrak{p}}(M);\:0\leq p\leq n). $$ 

6.3 Proposition  $ \Delta\alpha = 0 $ if and only if  $ d\alpha = 0 $ and  $ \delta\alpha = 0 $.

PROOF Clearly  $ \Delta\alpha = 0 $ if  $ d\alpha = 0 $ and  $ \delta\alpha = 0 $. Now,

 $$ \langle\Delta\alpha,\alpha\rangle=\langle(d\delta+\delta d)\alpha,\alpha\rangle=\langle\delta\alpha,\delta\alpha\rangle+\langle d\alpha,d\alpha\rangle. $$ 

Thus if  $ \Delta\alpha = 0 $, it follows that  $ d\alpha = 0 $ and  $ \delta\alpha = 0 $.

Corollary The only harmonic functions $(\Delta f = 0)$ on a compact, connected, oriented, Riemannian manifold are the constant functions.

##### THE HODGE THEOREM

6.4 Definition We shall let $\Delta^{*}$ denote the adjoint of the Laplacian on $E^{*}(M)$. This operator is, of course, precisely $\Delta$ itself since the Laplacian is self-adjoint on $E^{*}(M)$, and usually we make no distinction between $\Delta$ and $\Delta^{*}$. However, this distinction will be important for the form of the following definition.

We shall be interested in finding necessary and sufficient conditions for there to exist a solution  $ \omega $ of the equation  $ \Delta\omega = \alpha $. Suppose that  $ \omega $ is a solution of  $ \Delta\omega = \alpha $. Then

 $$ \langle\Delta\omega,\varphi\rangle=\langle\alpha,\varphi\rangle\quad\mathrm{f o r~a l l~}\varphi\in E^{\mathfrak{p}}(M), $$ 

from which it follows that

 $$ \langle\omega,\Delta^{*}\varphi\rangle=\langle\alpha,\varphi\rangle\quad\mathrm{f o r~a l l~}\varphi\in E^{\mathfrak{p}}(M). $$ 

Now, (2) suggests that we can view a solution of $\Delta\omega = \alpha$ as a certain type of linear functional on $E^{p}(M)$, namely, $\omega$ determines a bounded linear functional $l$ on $E^{p}(M)$ by

 $$ l(\beta)=\langle\omega,\beta\rangle; $$ 

and in view of (2), the functional I satisfies

 $$ l(\Delta^{*}\varphi)=\langle\alpha,\varphi\rangle\quad\mathrm{f o r~a l l~}\varphi\in E^{*}(M). $$ 

This view of a solution turns out to be extremely useful, for it will allow us to bring various techniques of functional analysis to bear on the problem of solving $\Delta\omega = \alpha$. We shall call such a linear functional a weak solution of $\Delta\omega = \alpha$. That is, a weak solution of $\Delta\omega = \alpha$ is a bounded linear functional $l: E^p(M) \to \mathbb{R}$ such that

 $$ l(\Delta^{*}\varphi)=\langle\alpha,\varphi\rangle\quad\mathrm{f o r~a l l~}\varphi\in E^{\mathfrak{p}}(M). $$ 

Later we will deal with weak solutions of a general partial differential operator $L$ defined on an open set in Euclidean space, and in place of $\Delta^{*}$ in (5), there will be the formal adjoint $L^{*}$ of $L$ (see 6.24(3) and 6.31).

We have seen that each ordinary solution  $ \omega \in E^p(M) $ of  $ \Delta\omega = \alpha $ determines a weak solution by (3). It turns out that the major effort of this chapter will be to prove a regularity theorem which says that the converse of this is true; that is, each weak solution determines an ordinary solution. The main step in proving this converse is to show that if  $ l $ is a weak solution of  $ \Delta\omega = \alpha $, then  $ l $ is represented by a smooth form  $ \omega $ in the sense that there is a form  $ \omega \in E^p(M) $ such that (3) holds. That the form  $ \omega $ is then an ordinary solution follows from the fact that

 $$ \langle\Delta\omega,\beta\rangle=\langle\omega,\Delta^{*}\beta\rangle=l(\Delta^{*}\beta)=\langle\alpha,\beta\rangle $$ 

for all  $ \beta \in E^p(M) $, which implies that  $ \Delta\omega = \alpha $.

6.5 Regularity Theorem Let  $ \alpha \in E^p(M) $, and let  $ l $ be a weak solution of  $ \Delta\omega = \alpha $. Then there exists  $ \omega \in E^p(M) $ such that

 $$ l(\beta)=\langle\omega,\beta\rangle $$ 

for every  $ \beta \in E^p(M) $. Consequently,  $ \Delta\omega = \alpha $.

We shall assume Theorem 6.5 for the moment as well as the following.

6.6 Theorem Let $\{\alpha_n\}$ be a sequence of smooth $p$-forms on $M$ such that $\|\alpha_n\| \leq c$ and $\|\Delta\alpha_n\| \leq c$ for all $n$ and for some constant $c > 0$. Then a subsequence of $\{\alpha_n\}$ is a Cauchy sequence in $E^p(M)$.

We will begin the machinery necessary for the proofs of Theorems 6.5 and 6.6 in the unit beginning with 6.15. We eventually return to the proofs of Theorems 6.5 and 6.6 in 6.32 and 6.33 respectively. Meanwhile, we shall assume the two theorems as proved and shall proceed to the Hodge theorem.

### 6.7 Definition We let

 $$ H^{\mathfrak{p}}=\{\omega\in E^{\mathfrak{p}}(M)\colon\Delta\omega=0\}. $$ 

The elements of  $ H^{p} $ are called harmonic p-forms.

6.8 The Hodge Decomposition Theorem For each integer $p$ with $0 \leq p \leq n$, $H^p$ is finite dimensional, and we have the following orthogonal direct sum decompositions of the space $\mathcal{E}^p(M)$ of smooth $p$-forms on $M$:

 $$ \begin{aligned}{E^{p}(M)}&{{}=\Delta(E^{p})\oplus H^{p}}\\ {}&{{}=d\delta(E^{p})\oplus\delta d(E^{p})\oplus H^{p}}\\ {}&{{}=d(E^{p-1})\oplus\delta(E^{p+1})\oplus H^{p}.}\\ \end{aligned} $$ 

Consequently, the equation $\Delta\omega = \alpha$ has a solution $\omega \in E^p(M)$ if and only if the $p$-form $\alpha$ is orthogonal to the space of harmonic $p$-forms.

PROOF If $H^{p}$ were not finite dimensional, then $H^{p}$ would contain an infinite orthonormal sequence. But by Theorem 6.6, this orthonormal sequence would contain a Cauchy subsequence, which is impossible. Thus $H^{p}$ is finite dimensional.

It is sufficient to prove the decomposition in the first line of (1), for the other two lines of (1) then follow from 6.1(3), 6.2, and 6.3.

Let  $ \omega_1, \ldots, \omega_t $ be an orthonormal basis of  $ H^p $. Then an arbitrary form  $ \alpha \in E^p(M) $ can uniquely be written

 $$ \alpha=\beta+\sum_{i=1}^{i}\langle\alpha,\omega_{i}\rangle\omega_{i} $$ 

where $\beta$ lies in $(H^{p})^{\perp}$, the subspace of $E^{p}(M)$ consisting of all elements orthogonal to $H^{p}$. Thus we have an orthogonal direct sum decomposition

 $$ E^{{s}}(M)=(H^{{s}})^{\perp}\oplus H^{{s}}. $$ 

The theorem will be proved by showing that  $ (H^{p})^{\perp} = \Delta(E^{p}) $. We let H denote the projection operator of E^{p}(M) onto H^{p} so that H(\alpha) is the harmonic part of \alpha.

Now  $ \Delta(\bar{E}^p) \subset (H^p)^\perp $. For if  $ \omega \in E^p $ and  $ \alpha \in H^p $, then

 $$ \langle\Delta\omega,\alpha\rangle=\langle\omega,\Delta\alpha\rangle=0. $$ 

Conversely, we claim that  $ (H^v)^\perp \subset \Delta(E^v) $. In order to prove this, we first need the following inequality.

We claim that there is a constant c > 0 such that

 $$ \left\Vert\beta\right\Vert\leq c\left\Vert\Delta\beta\right\Vert\quad\mathrm{f o r~a l l}\quad\beta\in(H^{\mathfrak{s}})^{\bot}. $$ 

Suppose the contrary. Then there exists a sequence  $ \beta_j \in (H^p)^\perp $ with  $ \|\beta_j\| = 1 $ and  $ \|\Delta\beta_j\| \to 0 $. By Theorem 6.6, a subsequence of the  $ \beta_j $, which for convenience we can assume to be  $ \{\beta_j\} $ itself, is Cauchy. Thus  $ \lim_{j \to \infty} \langle \beta_j, \psi \rangle $ exists for each  $ \psi \in E^p(M) $. We define a linear functional  $ l $ on  $ E^p(M) $ by setting

 $$ l(\psi)=\operatorname*{l i m}_{j\to\infty}\langle\beta_{j},\psi\rangle\quad\mathrm{f o r}\quad\psi\in E^{p}(M). $$ 

Now l is clearly bounded, and

 $$ l(\Delta\varphi)=\operatorname*{l i m}_{j\to\infty}\langle\beta_{j},\Delta\varphi\rangle=\operatorname*{l i m}_{j\to\infty}\langle\Delta\beta_{j},\varphi\rangle=0, $$ 

so $l$ is a weak solution of $\Delta\beta = 0$. By Theorem 6.5, there exists $\beta \in E^p(M)$ such that $l(\psi) = \langle \beta, \psi \rangle$. Consequently, $\beta_j \to \beta$. Since $\|\beta_j\| = 1$ and $\beta_j \in (H^p)^\perp$, it follows that $\|\beta\| = 1$ and $\beta \in (H^p)^\perp$. But by Theorem 6.5, $\Delta\beta = 0$, so $\beta \in H^p$, which is a contradiction. Thus (4) is proved.

Now we shall use (4) to prove that $(H^p)^\perp \subset \Delta(E^p)$. Let $\alpha \in (H^p)^\perp$. We define a linear functional $I$ on $\Delta(E^p)$ by setting

 $$ I(\Delta\varphi)=\langle\alpha,\varphi\rangle\quad\mathrm{f o r~a l l~}\varphi\in E^{\mathfrak{p}}(M). $$ 

Now $l$ is well-defined; for if $\Delta\varphi_1 = \Delta\varphi_2$, then $\varphi_1 - \varphi_2 \in H^p$, so that $\langle \alpha, \varphi_1 - \varphi_2 \rangle = 0$. Also $l$ is a bounded linear functional on $\Delta(E^p)$, for let $\varphi \in E^p(M)$ and let $\psi = \varphi - H(\varphi)$. Then using (4), we obtain

 $$ \begin{aligned}{|I(\Delta\varphi)|}&{{}=|I(\Delta\psi)|=|\langle\alpha,\psi\rangle|\leq\|\alpha\|\|\psi\|}\\ {}&{{}\leq c\left\|\alpha\right\|.\|\Delta\psi\|=c\left\|\alpha\right\|\|\Delta\varphi\|.}\\ \end{aligned} $$ 

By the Hahn-Banach theorem [27, p. 228], $l$ extends to a bounded linear functional on $E^p(M)$. Thus $l$ is a weak solution of $\Delta\omega = \alpha$. By Theorem 6.5, there exists $\omega \in E^p(M)$ such that $\Delta\omega = \alpha$. Hence

 $$ (H^{p})^{\perp}=\Delta(E^{p}), $$ 

and the Hodge decomposition theorem is proved.

6.9 Definition We define the Green's operator $G: E^p(M) \to (H^p)^\perp$ by setting $G(\alpha)$ equal to the unique solution of $\Delta\omega = \alpha - H(\alpha)$ in $(H^p)^\perp$. We leave it to the reader as an exercise to prove that $G$ is a bounded self-adjoint linear operator which takes bounded sequences into sequences with Cauchy subsequences.

6.10 Proposition G commutes with $d$, $\delta$, and $\Delta$. In fact, $G$ commutes with any linear operator which commutes with the Laplacian $\Delta$.

PROOF Suppose that $T\Delta = \Delta T$ with, say, $T: E^p(M) \to E^q(M)$. Let $\pi_{(H^p)^\perp}$ denote the projection mapping of $E^p(M)$ onto $(H^p)^\perp$. By definition, $G = (\Delta \mid (H^p)^\perp)^{-1} \circ \pi_{(H^p)^\perp}$. Now, the fact that $T\Delta = \Delta T$ implies that $T(H^p) \subset H^q$; and since $(H^p)^\perp = \Delta(E^p)$, it implies also that $T((H^p)^\perp) \subset (H^q)^\perp$. It follows that

 $$ T\circ\pi_{(H^{\flat})^{\perp}}=\pi_{(H^{\flat})^{\perp}}\circ T, $$ 

and on  $ (H^{v})^{\perp} $,

 $$ T\circ\left(\Delta\bigm|(H^{p})^{\perp}\right)=\left(\Delta\bigm|(H^{q})^{\perp}\right)\circ T, $$ 

and hence on  $ (H^{v})^{\perp} $

 $$ T\circ\bigl(\Delta\bigm|(H^{p})^{\perp}\bigr)^{-1}=\bigl(\Delta\bigm|(H^{q})^{\perp}\bigr)^{-1}\circ T. $$ 

It follows from (1) and (3) that G commutes with T.

6.11 Theorem Each de Rham cohomology class on a compact oriented Riemannian manifold M contains a unique harmonic representative.

PROOF Let $\alpha$ be an arbitrary $p$-form on $M$. From the Hodge decomposition theorem and from the definition of the Green's operator $G$, we have

 $$ \alpha=d\delta G\alpha+\delta d G\alpha+H\alpha. $$ 

Since G, by 6.10, commutes with d, we have

 $$ \alpha=d\delta G\alpha+\delta G d\alpha+H\alpha. $$ 

Thus if  $ \alpha $ is a closed p-form,

(3)

 $$ \alpha=d\delta G\alpha+H\alpha, $$ 

so $H\alpha$ is a harmonic $p$-form in the same de Rham cohomology class as is $\alpha$. If two harmonic forms $\alpha_{1}$ and $\alpha_{2}$ differ by an exact form $d\beta$, then we have

 $$ 0=d\beta+(\alpha_{1}-\alpha_{2}). $$ 

But  $ d\beta $ and  $ (\alpha_{1}-\alpha_{2}) $ are orthogonal since

 $$ \langle d\beta,\alpha_{1}-\alpha_{3}\rangle=\langle\beta,\delta\alpha_{1}-\delta\alpha_{3}\rangle=\langle\beta,0\rangle=0. $$ 

Thus $d\beta=0$ and $\alpha_{1}=\alpha_{2}$. Thus there is a unique harmonic form in each de Rham cohomology class.

Corollary The de Rham cohomology groups for a compact, orientable, differentiable manifold are all finite dimensional.

PROOF Any differentiable manifold can be equipped with a Riemannian metric (Exercise 23 of Chapter 1), and so the corollary follows immediately from Theorem 6.11 and from the finite dimensionality (6.8) of the spaces $H^{p}$ of harmonic forms.

6.12 Let $M$ be a compact, oriented, differentiable manifold of dimension $n$. We define a bilinear function

 $$ H_{\mathbf{d e}\mathbf{R}}^{s}(M)\times\mathit{H}_{\mathbf{d e}\mathbf{R}}^{n-s}(M)\to\mathbb{R} $$ 

by sending

 $$ \left(\{\varphi\},\{\psi\}\right)\mapsto\int_{\mathcal{M}}\varphi\wedge\psi, $$ 

where $\varphi$ and $\psi$ are closed forms representing the cohomology classes $\{\varphi\}$ in $H_{\mathrm{de}\mathrm{R}}^{p}(M)$ and $\{\psi\}$ in $H_{\mathrm{de}\mathrm{R}}^{n-p}(M)$. Observe that the bilinear map (2) is well-defined. For example, if $\varphi_{1}$ is another representative of the de Rham class $\{\varphi\}$, then $\varphi_{1}=\varphi+d\xi$ for some form $\xi$, and by the special case of Stokes' theorem which is contained in the corollary of 4.9,

 $$ \begin{aligned}{\int_{\mathcal{M}}\varphi_{1}\wedge\psi=}&{{}\int_{\mathcal{M}}\varphi\wedge\psi}&{+}&{{}\quad\int_{\mathcal{M}}d\xi\wedge\psi}\\ {=}&{{}\int_{\mathcal{M}}\varphi\wedge\psi}&{+}&{{}\quad\int_{\mathcal{M}}d(\xi\wedge\psi)=\int_{\mathcal{M}}\varphi\wedge\psi.}\\ \end{aligned} $$ 

Observe also from its definition that the bilinear function (2) depends on the orientation on $M$.

6.13 Theorem (Poincaré duality for the de Rham cohomology of a compact oriented $n$-dimensional manifold $M$) The bilinear function 6.12(2) is a non-singular pairing and consequently determines isomorphisms of $H_{\mathrm{de}^{\mathbb{R}}}^{n-\mathbb{P}}(M)$ with the dual space of $H_{\mathrm{de}^{\mathbb{R}}}^{\mathbb{P}}(M)$:

 $$ H_{\mathrm{d e}\mathbf{R}}^{n-p}(M)\cong\big(H_{\mathrm{d e}\mathbf{R}}^{p}(M)\big)^{*}. $$ 

PROOF Given a non-zero cohomology class $\{\varphi\} \in H_{\mathrm{deR}}^{p}(M)$, we must find a non-zero cohomology class $\{\psi\} \in H_{\mathrm{deR}}^{n-p}(M)$ such that $\left(\{\varphi\},\{\psi\}\right) \neq 0$. Choose a Riemannian structure on $M$. We can assume, according to 6.11, that $\varphi$ is the harmonic representative of $\{\varphi\}$. Since the cohomology class $\{\varphi\}$ is not zero, $\varphi$ is not identically zero. Since $* \Delta = \Delta^*$, it follows that $* \varphi$ is also harmonic, and therefore closed by 6.3, and so $* \varphi$ represents a cohomology class $\{*\varphi\} \in H_{\mathrm{deR}}^{n-p}(M)$. Now

 $$ \left(\{\varphi\},\{\ast\varphi\}\right)=\int_{M}\varphi\wedge\ast\varphi=\|\varphi\|^{2}\neq0. $$ 

Thus the pairing 6.12(2) is non-singular, and the isomorphism (1) follows from 2.7.

Corollary If $M$ is a compact, connected, orientable, differentiable manifold of dimension $n$, then $H_{\mathrm{de}\, \mathbb{R}}^n(M) \cong \mathbb{R}$.

6.14 Remark The real continuous singular homology groups $H_{p}(M;\mathbb{R})$ are defined just as in 4.16, with the exception that all continuous simplices in $M$ are allowed, not just differentiable simplices. The isomorphism 5.37(1) holds for the continuous case exactly as for the differentiable theory. By combining 6.13 with the de Rham theorem 5.36, with the canonical isomorphism 5.32(5) of the differentiable with the continuous real singular homology of $M$, and with the isomorphism 5.37(1) for the continuous real cohomology and homology, we obtain the Poincaré duality between the real singular cohomology and the real singular homology of $M$:

 $$ H_{\Delta}^{p}(M;\mathbb{R})\cong H_{n-p}(M;\mathbb{R}). $$ 

##### SOME CALCULUS

We now begin to develop the machinery necessary for the proofs of Theorems 6.5 and 6.6.

6.15 Notation We shall be using multi-index notation  $ \alpha = (\alpha_1, \ldots, \alpha_n) $ where the  $ \alpha_i $ are integers. We let  $ |\alpha| $ denote the ordinary Euclidean norm of  $ \alpha $; that is,

 $$ |\alpha|=(\alpha_{1}^{2}+\cdots+\alpha_{n}^{2})^{1/2}, $$ 

and if the  $ \alpha_{i} $ are all non-negative, then we let

 $$ [\alpha]=\alpha_{1}+\cdots+\alpha_{n}. $$ 

If  $ \alpha $ and  $ \eta $ are both  $ n $-tuples of integers, then

 $$ \begin{array}{r}{\eta^{\alpha}=\eta_{1}^{\alpha_{1}}\cdots\eta_{n}^{\alpha_{n}},\quad\mathrm{w h e r e~w e~s e t~0^{o}=1.}}\end{array} $$ 

We shall use $x_{i}$ for the $i$th canonical coordinate function on $\mathbb{R}^{n}$, and let

 $$ x=(x_{1},\ldots,x_{n}). $$ 

The $\alpha$th derivative operator $D^{\alpha}$ is defined for each $n$-tuple $\alpha$ of nonnegative integers by

 $$ D^{\alpha}{}_{u}=\left(\frac{1}{i}\right)^{[\alpha]}\frac{\partial^{[\alpha]}{}_{u}}{\partial x_{1}^{\alpha_{1}}\cdots\partial x_{n}^{\alpha_{n}}}, $$ 

where  $ i = \sqrt{-1} $. (The addition of the factor of i will be convenient later.)

We let $\mathcal{P}$ denote the complex vector space consisting of $C^\infty$ functions defined on $\mathbb{R}^n$ which have values in complex $m$ space $\mathbb{C}^m$ and are periodic of period $2\pi$ in each variable. I would suggest that the reader assume $m$ to be 1 for the first reading of this section since that case contains all of the essential ideas and the computations are somewhat simpler. We will arrange the notation so that it is essentially the same for general $m$. One note of caution concerning the notation is this. If $\gamma, \beta \in \mathbb{C}^m$, then $\gamma \cdot \beta$ means the Hermitian product $\gamma_1 \overline{\beta}_1 + \cdots + \gamma_m \overline{\beta}_m$. If $m$ happens to be 1, then $\gamma \cdot \beta$ means $\gamma \beta$. The associated norm is denoted by $|\gamma|$.

If $\varphi, \psi \in \mathcal{P}$, then $\varphi \cdot \psi$ is the complex-valued function which is the Hermitian product of $\varphi$ and $\psi$; that is,

 $$ \varphi\cdot\psi=\varphi_{1}\overline{{\psi_{1}}}+\cdots+\varphi_{m}\overline{{\psi_{m}}}. $$ 

We let  $ |\psi| $ denote the real-valued function

 $$ |\psi|=(\psi\cdot\psi)^{1/2}. $$ 

If $\varphi \in \mathcal{P}$ and if $f$ is a periodic complex-valued $C^\infty$ function on $\mathbb{R}^*$ (all periods always $2\pi$), then $\varphi f$ shall denote the element of $\mathcal{P}$ whose $i$th component function is $\varphi_i f$; that is,

 $$ \varphi f=(\varphi_{1}f,\ldots,\varphi_{m}f). $$ 

Let  $ Q \subset \mathbb{R}^n $ be the open cube

 $$ \mathcal{Q}=\{p\in\mathbb{R}^{n}\colon0<x_{i}(p)<2\pi,i=1,\ldots,n\}. $$ 

We shall be introducing a number of different norms on $\mathcal{P}$. By $\|\psi\|$ we shall mean the ordinary $L_{2}$ norm of $\psi$ over $Q$,

 $$ \|\psi\|=\frac{1}{(2\pi)^{n/2}}\biggl(\int_{Q}\psi\cdot\psi\biggr)^{1/2}, $$ 

and  $ \langle\psi,\varphi\rangle $ shall denote the  $ L_{2} $ inner product,

 $$ \langle\psi,\varphi\rangle=\frac{1}{(2\pi)^{n}}\int_{Q}\psi\cdot\varphi. $$ 

The norm  $ \|\psi\|_{\infty} $ shall denote the uniform norm of  $ \psi $,

 $$ \left\lVert{\psi}\right\rVert_{\infty}=\operatorname*{s u p}_{Q}\left\lvert{\psi}\right\rvert. $$ 

6.16 Some Facts about Fourier Series If $\varphi \in \mathcal{P}$ and if $\xi = (\xi_1, \ldots, \xi_n)$ where the $\xi_i$ are integers, then the $\xi$th Fourier coefficient $\varphi_i \in \mathbb{C}^m$ is defined by

 $$ \varphi_{\xi}=\frac{1}{(2\pi)^{n}}\int_{Q}\varphi(x)e^{-i x\cdot\xi}d x, $$ 

where  $ x \cdot \xi = x_{1} \xi_{1} + \cdots + x_{n} \xi_{n} $

First we are going to show that the Fourier series  $ \sum_{\ell} \varphi_{\ell} e^{i\pi\cdot\ell} $ of  $ \varphi $ converges uniformly to  $ \varphi $. Let an integer  $ k > 0 $ be given. By integrating (1) repeatedly by parts, differentiating  $ \varphi $ and integrating  $ e^{-i\pi\cdot\ell} $, and observing that the boundary terms drop out since the integrand is periodic, one sees that there is a constant  $ c_{k}^{\prime} $ depending on  $ \varphi $ and its derivatives up to order at most  $ 2nk $ such that

 $$ |\varphi_{\xi}|\leq\frac{c_{k}^{\prime}}{(\prod\xi_{i})^{3k}}\quad\mathrm{f o r~a l l}\quad\xi\not\equiv0, $$ 

where $\prod\xi_{i}$ denotes the product of all the non-zero $\xi_{i}$. It follows that there is a constant $c_{k}$ such that

 $$ |\varphi_{\xi}|\leq\frac{c_{k}}{(1+|\xi|^{2})^{k}}\quad\mathrm{f o r~a l l~\xi.~} $$ 

Consider now the question of convergence of the series  $ \sum_{\xi} (1 + |\xi|^2)^{-k} $. If we let

 $$ S_{j}=\Big\{\xi=(\xi_{1},\ldots,\xi_{n})\colon\operatorname*{m a x}_{1\leq i\leq n}|\xi_{i}|=j\Big\}, $$ 

then the number of elements of $S_i$ is at most $2n(2j+1)^{n-1}$, and for each $\xi \in S_i$, $|\xi|^2 \geq j^2$, so that

 $$ s_{j}=\sum_{\xi\in S_{j}}\frac{1}{(1+|\xi|^{2})^{k}}\leq\frac{2n(2j+1)^{n-1}}{(1+j^{2})^{k}}\leq c j^{n-1-2k} $$ 

for $j \geq 1$, where $c$ is a constant depending only on $n$. Consequently,

 $$ \begin{array}{r c c c l}{\displaystyle\sum_{\xi}\frac{1}{(1+|\xi|^{2})^{k}}}&{=}&{1+\sum_{j=1}^{\infty}s_{j}}&{\leq}&{1+c\sum_{j=1}^{\infty}\frac{1}{j^{1+2k-n}},}\\ \end{array} $$ 

and so the series  $ \sum_{k} (1 + |\xi|^{2})^{-k} $ converges for  $ 1 + 2k - n > 1 $, or in other words, for

 $$ k\geq\left[\frac{n}{2}\right]+1, $$ 

where  $ [n/2] $ denotes the greatest integer less than or equal to n/2. It would be an interesting exercise for the reader to reach the same conclusion by using an integral test.

It follows from (3) that if we take  $ k \geq [n/2] + 1 $ as in (7), then the Fourier series

 $$ \sum_{\ell}\varphi_{\ell}e^{i\alpha\cdot\ell} $$ 

converges uniformly to some continuous function $\Phi$. We claim that $\Phi = \varphi$. This is of course due to the completeness of the trigonometric system and may be deduced as follows from the Stone-Weierstrass theorem [13], [27]. Let $\psi = \varphi - \Phi$, and let $t \in \mathcal{P}$ be a trigonometric polynomial; that is, $t$ is a finite linear combination of terms of the form $a_t e^{i x \cdot \xi}$ for $a_t \in \mathbb{C}^m$. Then since $\varphi$ and $\Phi$ have the same Fourier coefficients,

 $$ \int_{Q}\boldsymbol{\psi}\cdot\boldsymbol{t}=0. $$ 

Now if $\varepsilon > 0$ is given, then by the Stone-Weierstrass theorem there is a trigonometric polynomial $t \in \mathcal{P}$ such that $\|\psi - t\|_\infty < \varepsilon$. Thus, using (9), we see that

 $$ \bigg|\int_{Q}\psi\cdot\psi\bigg|=\bigg|\int_{Q}\psi\cdot(\psi-t)\bigg|\leq\varepsilon(2\pi)^{n}\|\psi\|. $$ 

Consequently  $ \|\psi\| \leq \varepsilon $. But  $ \varepsilon > 0 $ was arbitrary and  $ \psi $ is continuous, so  $ \psi = 0 $. Thus the Fourier series of a periodic  $ C^\infty $ function  $ \varphi $ converges uniformly to  $ \varphi $,

 $$ \varphi(x)=\sum_{\xi}\varphi_{\xi}e^{i x\cdot\xi}. $$ 

It follows from integration by parts that the $\xi$th Fourier coefficient of $D^{\alpha}\varphi$ is $\xi_{1}^{\alpha_{1}}\cdots\xi_{n}^{\alpha_{n}}\varphi_{\xi}$. Thus

 $$ D^{a}\varphi(x)=\sum_{\xi}\xi^{a}\varphi_{\xi}e^{i x\cdot\xi}. $$ 

From (11) and the orthogonality of the trigonometric system, we obtain the Parseval identity:

 $$ \int_{Q}|\varphi|^{2}=(2\pi)^{n}\sum_{\ell}|\varphi_{\ell}|^{2}. $$ 

Applying (13) to  $ D^{\alpha}\varphi $, we obtain

 $$ \Vert D^{\alpha}\varphi\Vert^{2}=\sum_{\xi}\xi^{2\alpha}|\varphi_{\xi}|^{2}. $$ 

It follows from (14) that given a non-negative integer $t$, there is a constant $c$ greater than zero and depending only on $t$ and $n$ such that

 $$ \begin{array}{r l r l r}{c\displaystyle\sum_{\xi}(1+\vert\xi\vert^{2})^{t}\vert\varphi_{\xi}\vert^{2}}&{\leq}&{\displaystyle\sum_{[\alpha]=0}^{t}\Vert D^{\alpha}\varphi\Vert^{2}}&{\leq}&{\displaystyle\sum_{\xi}(1+\vert\xi\vert^{2})^{t}\vert\varphi_{\xi}\vert^{2}.}\end{array} $$ 

6.17 The Sobolev spaces  $ H_s $ Let  $ \delta $ denote the complex vector space consisting of all sequences of complex vectors in  $ \mathbb{C}^m $ indexed by  $ n $-tuples of integers  $ \xi = (\xi_1, \ldots, \xi_n) $. Thus if  $ u \in \mathcal{B} $,  $ u = \{u_\xi\} $ where  $ \xi $ runs over all  $ n $-tuples of integers and where each  $ u_\xi \in \mathbb{C}^m $. For each integer  $ s $ (positive, negative, or zero) the Sobolev space  $ H_s $ is the subspace of  $ \delta $ defined by

 $$ H_{s}=\Big\{u\in\mathbb{S}\colon\sum_{\xi}(1+\vert\xi\vert^{2})^{s}\vert u_{\xi}\vert^{2}<\infty\Big\}. $$ 

It follows from the Schwarz inequality that

 $$ \begin{array}{r l}&{\bigg|\sum_{\xi}(1+\vert\xi\vert^{2})^{(s+t)/2}u_{\xi}\cdot v_{\xi}\bigg\rvert^{2}\leq\bigg(\sum_{\xi}(1+\vert\xi\vert^{3})^{s}\vert u_{\xi}\vert^{2}\bigg)\left(\sum_{\xi}(1+\vert\xi\vert^{2})^{t}\vert v_{\xi}\vert^{2}\right);}\end{array} $$ 

hence the left-hand side of (2) is finite whenever each member of the right-hand side is finite. We can therefore define an inner product on  $ H_{s} $ by

 $$ \langle u,v\rangle_{s}=\sum_{\xi}(1+\vert\xi\vert^{2})^{s}u_{\xi}\cdot v_{\xi}. $$ 

The associated norm is

 $$ \left\Vert{u}\right\Vert_{s}=\left\langle{u,u}\right\rangle_{s}^{1/2}. $$ 

It also follows from (2) that  $ \langle u, v \rangle_s $ exists if  $ u \in H_t $ and  $ v \in H_{t'} $, where  $ (t + t')/2 = s $.

Since $H_{s}$ is simply an $l_{2}$-space in which the measure space is the set of all $n$-tuples of integers $\xi$, and the measure is the counting measure weighted by $(1 + |\xi|^{2})^{s}$, it follows that $H_{s}$ is a Hilbert space.

We define a linear transformation  $ K^{t} $ on S for each integer t by setting

 $$ (K^{t}u)_{\xi}=(1+|\xi|^{2})^{t}u_{\xi}. $$ 

Finally, we identify $\mathcal{P}$ with a subspace of $\mathcal{S}$ by associating with each $\varphi \in \mathcal{P}$ its sequence of Fourier coefficients $\{\varphi_k\}$. In view of 6.16(12) we can extend the derivative operator $D^a$ from $\mathcal{P}$ to all of $\mathcal{S}$ by setting

 $$ (D^{a}u)_{\xi}=\xi^{a}u_{\xi}. $$ 

The inequality 6.16(3) together with 6.16(7) shows that the more differentiable a function is, the greater the order $s$ of the Sobolev space $H_s$ in which its sequence of Fourier coefficients lies. In particular, $\mathcal{P} \subset H_s$ for each $s$. Moreover, $\mathcal{P}$ is dense in each $H_s$ since each $u \in H_s$ for which all but a finite number of the $u_s$ are zero belongs to $\mathcal{P}$. We consider elements of the Sobolev spaces $H_s$ as formal Fourier series or “generalized functions.” A fundamental lemma due to Sobolev says that if $u \in H_s$ for sufficiently large $s$, then the formal Fourier series determined by $u$ actually converges to a function with a certain number of derivatives depending on $s$. This lemma will be one of the key steps in the proof of the regularity theorem, for it will allow us to conclude that a generalized solution of a partial differential equation which belongs to a sufficiently high Sobolev space is an actual solution.

Some salient features of the $H_{s}$ spaces are collected in the following theorem, which is divided into parts (a)-(j).

### 6.18 Theorem

(a) Let s be a non-negative integer. Then there are constants c and  $ c' $, depending at most on s and n, such that

 $$ c\left\Vert{\varphi}\right\Vert_{s}\leq\sum_{\left\lceil{z}\right\rceil=0}^{s}\left\Vert{D^{\alpha}\varphi}\right\Vert\leq c^{\prime}\left\Vert{\varphi}\right\Vert_{s}{~f o r~a l l~}\varphi\in\mathcal{P}. $$ 

Moreover, for the case $s=0$, we actually have the equality

 $$ \left\lVert{\varphi}\right\rVert=\left\lVert{\varphi}\right\rVert_{0}{~f o r~a l l~}\varphi\in\mathcal{P}. $$ 

(b) If $t < s$, then $\|u\|_t \leq \|u\|_s$, so $H_s \subset H_t$. Thus the union of the $H_s$ spaces over all integers $s$ is a subspace of $\mathbb{S}$, which we denote by $H_{-\infty}$.

(c)  $ \mathcal{P} $ is a dense subspace of  $ H_{s} $ for each s.

(d) $K^{t}$ is an isometry of $H_{s}$ onto $H_{s-2t}$ with inverse $K^{-t}$,

(3)

 $$ \left\Vert u\right\Vert_{s}=\left\Vert K^{t}u\right\Vert_{s-2t}; $$ 

and  $ K^t $ maps  $ \mathcal{P} $ into  $ \mathcal{P} $. If  $ \varphi \in \mathcal{P} $ and  $ t \geq 0 $, then

(4)

 $$ K^{t}\varphi=\left(1-\sum_{i=1}^{n}\frac{\partial^{2}}{\partial x_{i}^{2}}\right)^{t}\varphi. $$ 

Moreover, for all s and t

 $$ \langle u,v\rangle_{s}=\langle u,K^{t}v\rangle_{s-t}=\langle K^{t}u,v\rangle_{s-t}\quad{f o r~}u,v\in H_{s}. $$ 

(e) Schwartz Inequality If  $ u \in H_{s+t} $ and  $ v \in H_{s-t} $, then

 $$ |\left\langle u,v\right\rangle_{s}|\leq\left\|u\right\|_{s+t}\left\|v\right\|_{s-t}. $$ 

(f) If  $ u \in H_{s+t} $, then

 $$ \left\Vert{u}\right\Vert_{s+t}=\operatorname*{s u p}_{\stackrel{v\in H_{s-t}}{v\neq0}}\frac{|\langle u,v\rangle_{s}|}{\left\Vert{v}\right\Vert_{s-t}}. $$ 

(g) Peter-Paul Inequality Given integers $t^{\prime}<t<t^{\prime\prime}$ and $\varepsilon>0$, there is a constant $c(\varepsilon)>0$ such that

 $$ \left\|{u}\right\|_{t}{}^{2}\leq\varepsilon\left\|{u}\right\|_{t^{\prime}}{}^{2}+c(\varepsilon)\left\|{u}\right\|_{t^{\prime}}{}^{2} $$ 

for all $u \in H_{t^*}$. (We refer to this inequality as the Peter-Paul inequality in view of the comparison with part (b), although the morality has been twisted around. Rather than robbing Peter to pay Paul, here we are paying Paul ($\|u\|_{t^*}$) in order to rob Peter ($\|u\|_{t^*}$).)

(h)  $ D^{\alpha} $ is a bounded operator from  $ H_{s+[\alpha]} $ to  $ H_{s} $ for each s; indeed,

 $$ \|D^{\alpha}u\|_{s}\leq\|u\|_{s+[\alpha]}\quad{f o r~a l l}\quad u\in H_{s+[\alpha]}. $$ 

(i) Let $\omega$ be a $C^{\infty}$ complex-valued periodic function on $\mathbb{R}^{n}$. Then given an integer $s$, these are positive integers $c$ and $c^{\prime}$, with $c$ depending only on $s$ and $n$, and $c^{\prime}$ depending on $s, n$, and on $\omega$ and its derivatives, such that

 $$ \left\Vert{\omega\varphi}\right\Vert_{s}\leq c\left\Vert{\omega}\right\Vert_{\infty}\left\Vert{\varphi}\right\Vert_{s}+c^{\prime}\left\Vert{\varphi}\right\Vert_{s-1},\quad{f o r~\varphi\in\mathcal{P}.~} $$ 

In particular, there is a constant $c^{\prime \prime}$ depending on $\omega$, $s$, and $n$ such that

 $$ \left\lVert{\omega\varphi}\right\rVert_{s}\leq c^{\prime\prime}\left\lVert{\varphi}\right\rVert_{s}, $$ 

so multiplication by $\omega$ extends by continuity to a bounded operator on $H_{s}$

(j) Let $\omega$ be a $C^{\infty}$ complex-valued periodic function on $\mathbb{R}^{n}$. Then given an integer $s$, there is a positive constant $c$ such that

 $$ \left|\left\langle\omega u,v\right\rangle_{s}-\left\langle u,\bar{\omega}v\right\rangle_{s}\right|\leq c(\left\|u\right\|_{s}\left\|v\right\|_{s-1}+\left\|u\right\|_{s-1}\left\|v\right\|_{s}) $$ 

for each $u, v \in H_{s}$. For the case $s = 0$, we have

 $$ \langle\omega u,v\rangle_{0}=\langle u,\bar{\omega}v\rangle_{0}. $$ 

PROOF The inequality (1) follows from 6.16(15) and the fact that whenever $a_{1},\ldots,a_{n}$ are positive numbers, then

 $$ \frac{1}{n}\Big(\sum_{i=1}^{n}a_{i}\Big)^{2}\leq\sum_{i=1}^{n}a_{i}^{2}\leq\Big(\sum_{i=1}^{n}a_{i}\Big)^{2}. $$ 

The equality (2) is simply the Parseval identity 6.16(13).

Part (b) is obvious. The fact that 6.16(3) holds for each integer $k > 0$ implies that $\{\varphi_{\xi}\} \in H_s$ whenever $\varphi \in \mathcal{P}$, and as we have already indicated in the remarks immediately preceding the theorem, $\mathcal{P}$ is dense in $H_s$ since each $u \in H_s$ for which all but a finite number of the $u_\xi$ are zero belongs to $\mathcal{P}$.

The identities (3) and (5) in (d) are obvious; that the inner products are all well-defined follows from the remark immediately following 6.17(4). Let $\varphi \in \mathcal{P}$. We have $K^t\varphi = \{(1 + |\xi|^2)^t\varphi_\xi\}$. It follows from 6.16(3) and (7) and from the fact that there exists the inequality

 $$ \xi^{2\alpha}\leq(1+\vert\xi\vert^{2})^{[\alpha]} $$ 

that the series

 $$ \sum_{\xi}(1+\vert\xi\vert^{2})^{t}\varphi_{\xi}e^{i x\cdot\xi} $$ 

and all its formal derivatives

 $$ \sum_{\xi}D^{\alpha}(1+\vert\xi\vert^{2})^{t}\varphi_{\xi}e^{i x\cdot\xi}=\sum_{\xi}\xi^{\alpha}(1+\vert\xi\vert^{2})^{t}\varphi_{\xi}e^{i x\cdot\xi} $$ 

converge uniformly. Thus (12) converges to a periodic $C^\infty$ function and therefore is an element of $\mathcal{P}$. Hence $K^t$ maps $\mathcal{P}$ into $\mathcal{P}$. For (4), simply observe that the $\xi$th Fourier coefficient of the right-hand side equals $(1 + |\xi|^2)^t \varphi_\xi$.

The Schwartz inequality (e) is none other than 6.17(2). It follows from (e) that

 $$ \left\Vert{u}\right\Vert_{s+t}\geq\operatorname*{s u p}_{v\in\underline{{H}}_{s-t\atop v\neq0}}\frac{|\langle u,v\rangle_{s}|}{\|v\|_{s-t}}. $$ 

To prove the equality in (f), let  $ v = K^{t} u $. Then by (d),

 $$ \left\|u\right\|_{s+t}=\frac{\left\langle u,u\right\rangle_{s+t}}{\left\|u\right\|_{s+t}}=\frac{\left\langle u,v\right\rangle_{s}}{\left\|v\right\|_{s-t}}. $$ 

To prove the Peter-Paul inequality (g), first observe that for any positive number y,

 $$ 1\leq y^{t^{\prime\prime}-t}+\;\left(\frac{1}{y}\right)^{t-t^{\prime}} $$ 

since either y or 1/y is greater than or equal to 1. If in (14) we let

 $$ y=e^{1/(t^{\prime\prime}-t)}(1+\vert\xi\vert^{3}), $$ 

we obtain

 $$ (1+|\xi|^{2})^{t}\leq\varepsilon(1+|\xi|^{2})^{t^{\prime}}+\varepsilon^{(t^{\prime}-t)/(t^{\prime\prime}-t)}(1+|\xi|^{2})^{t^{\prime}}, $$ 

from which the Peter-Paul inequality follows with

 $$ c(\varepsilon)=\varepsilon^{(t^{\prime}-t)/(t^{\prime \prime}-t)}. $$ 

The inequality in (h) follows from the inequality (11).

In part (i), the inequality (7) follows immediately from part (b) and inequality (6). To prove (6), we first consider the case in which $s \geq 0$. Let $\varphi \in \mathcal{P}$. Then by applying (1), we obtain

 $$ \begin{aligned}{\|\omega_{\varphi}\|_{s}}&{{}\leq\operatorname{c o n s t}\sum_{[\alpha]=0}^{s}\|D^{\alpha}\omega_{\varphi}\|}\\ {}&{{}\leq\operatorname{c o n s t}\sum_{[\alpha]=0}^{s}\|\omega D^{\alpha}\varphi\|+\operatorname{c o n s t}\sum_{[\alpha]=0}^{s}\|D^{\alpha}\omega_{\varphi}-\omega D^{\alpha}\varphi\|}\\ {}&{{}\leq c\|\omega\|_{\infty}\|\varphi\|_{s}+\operatorname{c o n s t}\sum_{[\alpha]=0}^{s-1}\|D^{\alpha}\varphi\|}\\ {}&{{}\leq c\|\omega\|_{\infty}\|\varphi\|_{s}+c^{\prime}\|\varphi\|_{s-1}.}\\ \end{aligned} $$ 

At the third stage we have used the fact that  $ D^{\alpha}\omega\varphi - \omega D^{\alpha}\varphi $ only contains derivatives of  $ \varphi $ up to order [ $ \alpha $] - 1. For s < 0 we have

 $$ \begin{aligned}{\|\omega\varphi\|_{s}^{2}}&{{}=\langle\omega\varphi,\omega\varphi\rangle_{s}=\langle\omega K^{-s}K^{s}\varphi,K^{s}\omega\varphi\rangle_{0}}\\ {}&{{}=\langle K^{-s}\omega K^{s}\varphi,K^{s}\omega\varphi\rangle_{0}+\langle(\omega K^{-s}-K^{-s}\omega)K^{s}\varphi,K^{s}\omega\varphi\rangle_{0}}\\ {}&{{}\leq|\langle K^{-s}\omega K^{s}\varphi,K^{s}\omega\varphi\rangle_{0}|+\left|\bigvee_{\lbrace\alpha\rbrace=0}^{-2s-1}a_{\alpha}D^{\alpha}K^{s}\varphi,K^{s}\omega\varphi\biggr\rangle_{0}\right|,}\\ \end{aligned} $$ 

where the  $ a_a $ are combinations of derivatives of  $ \omega $. Now, by the case  $ s \geq 0 $ of (i) we obtain

 $$ \begin{aligned}{|\langle K^{-s}\omega K^{s}\varphi,K^{s}\omega\varphi\rangle_{0}|}&{{}=|\langle\omega K^{s}\varphi,K^{s}\omega\varphi\rangle_{-s}|\leq\|\omega K^{s}\varphi\|_{-s}\|K^{s}\omega\varphi\|_{-s}}\\ {}&{{}\leq(c\|\omega\|_{\infty}\|K^{s}\varphi\|_{-s}+k^{\prime}\|K^{s}\varphi\|_{-s-1})(\|K^{s}\omega\varphi\|_{-s})}\\ {}&{{}=(c\|\omega\|_{\infty}\|\varphi\|_{s}+k^{\prime}\|\varphi\|_{s-1})\|\omega\varphi\|_{s}.}\\ \end{aligned} $$ 

As for the last term in (15),

 $$ \begin{aligned}{\left|\left\langle\sum_{[\epsilon]=0}^{-2s-1}a_{\epsilon}D^{\alpha}K^{\epsilon}\varphi,K^{\epsilon}\omega\varphi\right\rangle_{0}\right|}&{{}\leq\operatorname{c o n s t}\sum_{[\epsilon]=0}^{-2s-1}|\langle D^{\alpha}K^{\epsilon}\varphi,K^{\epsilon}\omega\varphi\rangle_{0}|}\\ {}&{{}\leq\operatorname{c o n s t}\sum_{[\epsilon]=0}^{-2s-1}\|D^{\alpha}K^{\epsilon}\varphi\|_{s}\|K^{\epsilon}\omega\varphi\|_{-s}}\\ {}&{{}\leq\operatorname{c o n s t}\sum_{[\epsilon]=0}^{-2s-1}\|K^{\epsilon}\varphi\|_{s+[\epsilon]}\|K^{\epsilon}\omega\varphi\|_{-s}}\\ {}&{{}\leq\operatorname{c o n s t}\|K^{\epsilon}\varphi\|_{-s-1}\|K^{\epsilon}\omega\varphi\|_{-s}}\\ {}&{{}\leq\operatorname{c o n s t}\|\varphi\|_{s-1}\|\omega\varphi\|_{s}.}\\ \end{aligned} $$ 

Thus for $s < 0$, (6) follows from (15), (16), and (17).

It is sufficient to prove (8) and (9) in part (j) on the dense subspace  $ \mathcal{P} $ of  $ H_s $. Observe that (9) follows immediately from the fact (1) that the  $ L_2 $-norm is identical with the Sobolev norm  $ \|\cdot\|_0 $ on  $ \mathcal{P} $. Let  $ \varphi, \psi \in \mathcal{P} $. We consider the case of (8) in which  $ s $ is negative. Using part (d) and equation (9), we obtain

 $$ \begin{aligned}{\langle\omega\varphi,\psi\rangle_{s}}&{{}=\langle\omega K^{-s}K^{s}\varphi,K^{s}\psi\rangle_{0}}\\ {}&{{}=\langle K^{-s}K^{s}\varphi,\bar{\omega}K^{s}\psi\rangle_{0}=\langle K^{s}\varphi,K^{-s}\bar{\omega}K^{s}\psi\rangle_{0}}\\ {}&{{}=\langle\varphi,\bar{\omega}\psi\rangle_{s}+\langle K^{s}\varphi,(K^{-s}\bar{\omega}-\bar{\omega}K^{-s})K^{s}\psi\rangle_{0}.}\\ \end{aligned} $$ 

It follows as in (17) that

 $$ |\langle\omega_{\Phi},\psi\rangle_{s}-\langle\varphi,\bar{\omega}\psi\rangle_{s}|\leq\mathrm{c o n s t}\|\varphi\|_{s}\|\psi\|_{s-1}. $$ 

By symmetry we also have

 $$ |\langle\omega\varphi,\psi\rangle_{s}-\langle\varphi,\bar{\omega}\psi\rangle_{s}|\leq\mathrm{c o n s t}\|\psi\|_{s}\|\varphi\|_{s-1}. $$ 

Thus (8) is proved for $s$ negative. The proof is similar for $s$ positive. The proof of Theorem 6.18 is complete.

6.19 Difference Quotients If $\varphi \in \mathcal{P}$, then the $\xi$th Fourier coefficient of the translate $\varphi(x + h)$ of $\varphi$ by an element $h \in \mathbb{R}^n$ is $e^{ih \cdot \xi} \varphi_\xi$. Thus if $u \in \mathcal{S}$ and $h \in \mathbb{R}^n$, we define the translate $u$ by $h$ to be the element

 $$ T_{h}(u)=\{e^{i h\cdot\xi}u_{\xi}\}\in\mathcal{S}. $$ 

The difference quotient of u determined by a non-zero h is the element

 $$ u^{h}=\frac{T_{h}(u)-u}{|h|}=\left\{\left(\frac{e^{i h\cdot\xi}-1}{|h|}\right)u\right\}\in\mathcal{S}. $$ 

So if  $ \varphi \in \mathcal{P} $, then  $ T_{h}(\varphi)(x) = \varphi(x + h) $ and

 $$ \varphi^{h}(x)=\frac{\varphi(x+h)-\varphi(x)}{|h|}. $$ 

Observe that if  $ u \in H_{s} $, then

 $$ \left\Vert T_{h}(u)\right\Vert_{s}=\left\Vert u\right\Vert_{s}, $$ 

so $T_h$ is an isometry on $H_s$. Thus, in particular, if $u \in H_s$, then also $u^h \in H_s$ for each $h$. It follows from the inequality

 $$ \begin{aligned}{\bigg|\frac{e^{i h\cdot\xi}-1}{|h|}\bigg|^{2}}&{{}=\bigg|\frac{(\operatorname{c o s}h\cdot\xi)-1}{|h|}\bigg|^{2}+\bigg|\frac{\operatorname{s i n}h\cdot\xi}{|h|}\bigg|^{2}=\frac{2(1-\operatorname{c o s}h\cdot\xi)}{|h|^{2}}}\\ {}&{{}=\frac{4\operatorname{s i n}^{2}(\frac{1}{2}h\cdot\xi)}{|h|^{2}}\leq\frac{(h\cdot\xi)^{2}}{|h|^{2}}\leq(1+|\xi|^{2})}\\ \end{aligned} $$ 

that if  $ u \in H_{s+1} $, then the  $ u^k $ are uniformly bounded in the  $ s $-norm. In fact,

 $$ \|u^{h}\|_{s}\leq\|u\|_{s+1}. $$ 

We shall need the converse of this, as follows.

6.20 Lemma Let  $ u \in H_s $, and assume that there is a constant  $ k $ such that  $ \|u^h\|_s \leq k $ for all non-zero  $ h \in \mathbb{R}^n $. Then  $ u \in H_{s+1} $.

PROOF For each positive integer N we let  $ u_{v} $ be the element of  $ H_{s} $ obtained by truncating u at N; that is,

 $$ (u_{N})_{\xi}=\left\{\begin{matrix}{u_{\xi}}&{\mathrm{i f}\quad|\xi|<N}\\ {0}&{\mathrm{o t h e r w i s e}.}\\ \end{matrix}\right. $$ 

We need only prove that the  $ \|u_N\|_{s+1} $ are uniformly bounded. Let  $ (e_1, \ldots, e_n) $ be the standard orthonormal basis of  $ \mathbb{R}^n $, and let  $ h = te_i $. Then

 $$ \bigg|\frac{e^{i h\cdot\xi}-1}{|h|}\bigg|^{2}=\bigg|\frac{e^{i t\xi_{i}}-1}{t}\bigg|^{2}\to|\xi_{i}|^{2}\quad\mathrm{a s}\quad t\to0. $$ 

Since there are only finitely many  $ \xi $ with  $ |\xi| < N $, and since by hypothesis

 $$ \sum_{|\xi|<N}(1+|\xi|^{2})^{s}\left|u_{\xi}\right|^{2}\left|\frac{e^{i h\cdot\xi}-1}{|h|}\right|^{2}\leq k^{2}, $$ 

it follows from (2) that

 $$ \sum_{|\xi|<N}(1+|\xi|^{2})^{s}\left|u_{\xi}\right|^{2}|\xi_{i}|^{2}\leq k^{2}. $$ 

Thus  $ \|u_N\|_s+1 = \sum_{|\xi|<N}(1 + |\xi|^2)^{s+1}|u_\xi|^2 \leq nk^2 + \|u\|_{s^2}^2 $, so the  $ \|u_N\|_s+1 $ are uniformly bounded, and consequently  $ u \in H_{s+1} $.

6.21 Associate with each $u \in H_{-\infty}$ the series $\sum u_{\xi} e^{ix \cdot \xi}$. It will be of fundamental importance in what follows to know when this series converges, and (if it converges) how differentiable its limit is. The answer is supplied by the following lemma due to Sobolev.

6.22 Sobolev Lemma If $t \geq [n/2] + 1$ and $u \in H_t$, then the series $\sum_{t} u_t e^{i x \cdot \xi}$ converges uniformly. Thus each $u \in H_t$ for $t \geq [n/2] + 1$ corresponds to a continuous function.

PROOF It is sufficient to demonstrate that the series converges absolutely,  $ \sum |u_{\xi}| < \infty $. Now,

 $$ \begin{align*}\sum_{|\xi|<N}|u_{\xi}|&=\sum_{|\xi|<N}(1+|\xi|^{2})^{-t/2}(1+|\xi|^{2})^{t/2}|u_{\xi}|\\&\leq\left(\sum_{|\xi|<N}(1+|\xi|^{2})^{-t}\right)^{1/2}\binom{\sum_{|\xi|<N}(1+|\xi|^{2})^{t}|u_{\xi}|^{2}}{||\xi||<N}\\&\leq\left(\sum_{|\xi|<N}(1+|\xi|^{2})^{-t}\right)^{1/2}\|u\|_{t}.\end{align*} $$ 

Thus the result follows from 6.16(7).

Corollary (a) If $u \in H_t$ where $t \geq [n/2] + 1 + m$, then $D^s u = \sum \xi^s u_\xi e^{i\pi \cdot\xi}$ converges uniformly for $(\alpha) \leq m$. Thus each $u \in H_t$ for this range of $t$ corresponds to a function $\sum u_\xi e^{i\pi \cdot\xi}$ of class $C^m$.

PROOF With $u \in H_t$ for $t \geq [n/2] + 1 + m$ and with $[\alpha] \leq m$, it follows from 6.18(h) that $D^x u \in H_{t-[\alpha]}$, where $t - [\alpha] \geq [n/2] + 1$. Thus it follows from the Sobolev lemma that $\sum \xi^x u_\xi e^{ix \cdot \xi}$ converges uniformly. Now this series is the $\alpha$th “formal” derivative of the series $\sum u_\xi e^{ix \cdot \xi}$. Thus $\sum u_\xi e^{ix \cdot \xi}$ is of class $C^m$.

Corollary (b) From the proof of 6.22 it follows that if  $ t \geq [n/2] + 1 $, then there is a constant  $ c > 0 $ such that if  $ \varphi \in \mathcal{P} $, then

 $$ \left\|\varphi\right\|_{\infty}\leq c\left\|\varphi\right\|_{t}. $$ 

Applying (1) to  $ D^{*} \varphi $ and using 6.18(h), we obtain

 $$ \left\|D^{\alpha}\varphi\right\|_{\infty}\leq c\left\|\varphi\right\|_{\mathfrak{t}+[\alpha]}. $$ 

6.23 Rellich Lemma Let  $ \{u^i\} $ be a sequence of elements of  $ H_t $ with  $ \|u^i\|_t \leq 1 $. If  $ s < t $, then there is a subsequence of  $ \{u^i\} $ which converges in  $ H_s $.

PROOF By assumption.

PROOF By assumption,

 $$ \sum_{\xi}(1+\vert\xi\vert^{2})^{t}\vert u_{\xi}^{t}\vert^{2}\leq1. $$ 

For each fixed $\xi$, elements of the sequence $\{|(1 + |\xi|^s)^{t/2}u_{\xi}^{t}|\}$ are all bounded by 1, so the sequence $\{(1 + |\xi|^s)^{t/2}u_{\xi}^{t}\}$ has a convergent subsequence in $\mathbb{C}^m$. By the usual diagonal process, one can select a subsequence $\{u^{t_i}\}$ such that the sequence $(1 + |\xi|^s)^{t/2}u_{\xi}^{t_i}$ converges in $\mathbb{C}^m$ for each fixed $\xi$. We claim that $\{u^{t_i}\}$ is Cauchy, and therefore convergent, in $H_s$ if $s < t$. Let $e > 0$ be given. Now,

 $$ \begin{aligned}{\|u^{j_{t}}-u^{j_{k}}\|_{s}^{2}=}&{{}\sum_{|\xi|<N}(1+|\xi|^{2})^{s-t}(1+|\xi|^{2})^{t}|u_{\xi}^{j_{t}}-u_{\xi}^{j_{k}}|^{2}}\\ {}&{{}+\sum_{|\xi|\geq N}(1+|\xi|^{2})^{s-t}(1+|\xi|^{2})^{t}|u_{\xi}^{j_{t}}-u_{\xi}^{j_{k}}|^{2}.}\\ \end{aligned} $$ 

The second sum in (2) is bounded by

 $$ N^{2(s-t)}\sum_{|\xi|\geq N}(1+|\xi|^{2})^{t}(|u_{\xi}^{j_{t}}|^{2}+2|u_{\xi}^{j_{t}}||u_{\xi}^{j_{k}}|+|u_{\xi}^{j_{k}}|^{2}), $$ 

which is $\leq4N^{2(s-t)}$ in view of (1). Since $s-t<0$, $4N^{2(s-t)}$ can be made less than $\varepsilon/2$ by taking $N$ large enough, say $N=N_{0}$. The first sum in (2) is then bounded by

 $$ \sum_{|\xi|<N_{0}}(1+|\xi|^{2})^{t}|u_{\xi}^{j_{t}}-u_{\xi}^{j_{k}}|^{2}, $$ 

and since there are only a finite number of terms in this sum and since the sequences $(1 + |\xi|^2)^{i/2}u_{\xi}^{j_i}$ converge for each fixed $\xi$, there is a constant $J > 0$ such that if $j_i$ and $j_k$ are greater than $J$, then (3) is less than $\varepsilon/2$. Thus for $j_i, j_k > J$, we have $\|u^{j_i} - u^{j_k}\|_s^2 < \varepsilon$, and the proof is complete.

6.24 Definitions A (linear) differential operator L of order l on the  $ C^{m} $-valued  $ C^{\infty} $ functions on  $ R^{n} $ consists of an  $ m \times m $ matrix  $ (L_{ij}) $ in which

 $$ {\cal L}_{i j}=\sum_{\{a\}=0}^{i}a_{i j}^{a}D^{a}, $$ 

and the $a_{ij}^{e}$ are $C^{\infty}$ complex-valued functions on $\mathbb{R}^{n}$, with at least one $a_{ij}^{e} \neq 0$ for some $i, j$ and for some $\alpha$ for which $|\alpha| = l$. A differential operator $L$ is a periodic differential operator, or an operator on $\mathcal{P}$, if, in addition, the $a_{ij}^{e}$ are periodic functions.

Let $L$ be a periodic differential operator, and let $\varphi \in \mathcal{P}$ with component functions $\varphi_1, \ldots, \varphi_m$. Then

 $$ L_{\Psi}=\left(\sum_{j}L_{1j}\varphi_{j},\ldots,\sum_{j}L_{m j}\varphi_{j}\right). $$ 

It follows from integration by parts that if we define the operator  $ L^{*} $ on  $ \mathcal{P} $ by

 $$ L_{i j}^{*}=\sum_{\{a\}=0}^{l}D^{a}\overline{{a_{j i}^{a}}} $$ 

so that the ith component of  $ L^{*}\phi $ is given by

 $$ (L^{*}\varphi)_{i}=\sum_{j=0}^{m}\sum_{[a]=-0}^{l}D^{a}(\overline{{a_{j i}^{a}}}\varphi_{j}), $$ 

then in the $L_{2}$ inner product on $\mathcal{P}$ we have

 $$ \langle L\varphi,\psi\rangle=\langle\varphi,L^{*}\psi\rangle $$ 

for $\varphi, \psi \in \mathcal{P}$. $L^{*}$ is called the formal adjoint of $L$. The word “formal” is used here to emphasize that $L^{*}$ is not the adjoint of $L$ on a Hilbert space. It is simply the adjoint relative to the $L_{2}$ inner product on $\mathcal{P}$.

6.25 Proposition Let L be a partial differential operator on $\mathcal{P}$ of order $l$, and let s be an integer. Then there are positive constants $c, k$, and $c',$ where $c$ depends only on $n, m, l$, and $s$, where $k$ is a bound on the absolute values of the coefficients of the highest order terms in $L$, and where $c'$ depends on $n, m, l$, and on all the coefficients of L and their derivatives up to order $l$, such that

 $$ \left\Vert{L\varphi}\right\Vert_{s}\leq c k\left\Vert{\varphi}\right\Vert_{s+l}+c^{\prime}\left\Vert{\varphi}\right\Vert_{s+l-1} $$ 

for all $\varphi \in \mathcal{P}$. In particular, there is a constant $c$ such that

 $$ \left\Vert L\varphi\right\Vert_{s}\leq c^{\prime\prime}\left\Vert\varphi\right\Vert_{s+1} $$ 

for all $\varphi \in \mathcal{P}$, so $L$ extends by continuity to a bounded operator from $H_{s+1}$ to $H_{s}$ for each $s$.

PROOF The inequality (2) is an immediate consequence of (1) and 6.18(b). As for (1), the case $m=1$ (in which elements of $\mathcal{P}$ are $\mathbb{C}^1$ valued functions and the operator $L$ is a single partial differential operator $\sum a^a D^a$ rather than a matrix) follows immediately from 6.18(h) and (i). The inequality (1) for general $m$ follows from the case $m=1$ and from the inequality $\|L\varphi\|_s \leq \sup_{i,j} \|L_{ij}\varphi_j\|_s$, where

 $ \varphi = (\varphi_1, \ldots, \varphi_m) \in \mathcal{P} $, and the constant depends only on  $ m $.

6.26 Remark If $L$ is an operator on $\mathcal{P}$ of order $l$, and if $\omega$ is a $C^\infty$ complex-valued function on $\mathbb{R}^n$, then the operator $M = \omega L - L\omega$, where $M\varphi = \omega(L\varphi) - L(\omega\varphi)$, is of order at most $l-1$. Consequently, given $s$, there is a positive constant such that

 $$ \left\Vert M\varphi\right\Vert_{s}\leq\mathrm{c o n s t}\left\Vert\varphi\right\Vert_{s+l-1} $$ 

for all  $ \varphi \in \mathcal{P} $.

6.27 Lemma If $\omega$ is a real-valued periodic $C^{\infty}$ function, and $L$ is a differential operator of order $l$ on $\mathcal{P}$, then there is a positive constant such that

 $$ |\langle L(\omega^{2}u),L u\rangle_{s}-\|L(\omega u)\|_{s}^{2}|\leq\mathtt{c o n s t}\left(\|u\|_{s+1}\|u\|_{s+l-1}\right) $$ 

for all  $ u \in H_{e+1} $.

 $$ \begin{aligned}{\mathtt{P R O O F}\quad|\langle L(\omega^{z}u),L u\rangle_{s}-\langle L(\omega u),L(\omega u)\rangle_{s}|}&{{}}\\ {}&{{}\leq|\langle\omega L(\omega u),L u\rangle_{s}-\langle L(\omega u),\omega L u\rangle_{s}|}\\ {}&{{}+|\langle L(\omega u),(\omega L-L\omega)u\rangle_{s}|}\\ {}&{{}+|\langle(L\omega-\omega L)(\omega u),L u\rangle_{s}|,}\\ \end{aligned} $$ 

and (1) follows by applying 6.18(j), 6.25(2), and 6.18(7) to the first term and applying the Schwartz inequality, 6.26(1), 6.25(2), and 6.18(7) to the last two terms.

##### ELLIPTIC OPERATORS

6.28 Definition Let L be a partial differential operator of order l. We write L as

 $$ {\cal L}=P_{t}(D)+\cdots+P_{0}(D), $$ 

where $P_{i}(D)$ is an $m \times m$ matrix each entry of which is a differential operator $\sum [a_{a}D^{a}$, homogeneous of order $j$, and where the $a_{a}$ are $C^{\infty}$ complex

 $ ^{[a]=i} $ valued functions on  $ \mathbb{R}^n $. We let  $ P_i(\xi) $ denote the matrix obtained by substituting  $ \xi^a $ for  $ D^a $ in  $ P_i(D) $, where  $ \xi = (\xi_1, \ldots, \xi_n) $ is a point in  $ \mathbb{R}^n $. L is said to be elliptic at the point  $ x \in \mathbb{R}^n $ if the matrix  $ P_i(\xi) $ is non-singular at x for each non-zero  $ \xi $. L is elliptic if it is elliptic at each x. Observe that ellipticity is a condition on the highest-order part of L only. Observe also that L is elliptic at x if and only if

 $$ L(\varphi^{\iota}u)(x)\neq0 $$ 

for each $C^{m}$-valued $C^{\infty}$ function $u$ such that $u(x) \neq 0$ and each smooth real-valued function $\varphi$ such that $\varphi(x) = 0$ but $d\varphi(x) \neq 0$, since for each such $\varphi$ and $u$,

 $$ L(\varphi^{l}u)(x)=P_{l}(D)(\varphi^{l}u)(x)=P_{l}(d\varphi|_{\alpha})(u(x)). $$ 

The advantage of this criterion (2) for ellipticity is that it generalizes to a coordinate-free definition of ellipticity on manifolds, as we shall see later.

The basic analytic property of an elliptic operator that we shall need is the following.

6.29 Fundamental Inequality Let L be an elliptic operator on  $ \mathcal{P} $ of order l, and let s be an integer. Then there is a constant c > 0 such that

 $$ \|u\|_{s+l}\leq c(\|L u\|_{s}+\|u\|_{s}) $$ 

for all  $ u \in H_{s+1} $.

PROOF It is sufficient to prove (1) for all $\varphi \in \mathcal{P}$. The proof consists of several parts. We first consider the case of an elliptic operator $L_0$ on $\mathcal{P}$ with constant coefficients, which consists of the leading term

$P_i(D)$ only. If $u \in \mathbb{R}^n$ with $u \neq 0$, and if $\xi \neq 0$, then since $P_i(\xi)$ is non-singular, we have $|P_i(\xi)u|^2 > 0$. It follows from the compactness of the unit sphere in $\mathbb{R}^n$ that there is a constant $c > 0$ such that

 $$ |P_{i}(\xi)u|^{2}\geq c $$ 

for all  $ u $ and  $ \xi $ such that  $ |u| = |\xi| = 1 $. From this it follows that

 $$ |P_{i}(\xi)u|^{\sharp}\geq c|\xi|^{\underline{{s}}l}|u|^{\underline{{s}}} $$ 

for all $u$ and $\xi$ in $\mathbb{R}^n$. Thus for $\varphi \in \mathcal{P}$, it follows from (2) and the fact that $L_0$ has constant coefficients that

 $$ \begin{aligned}{\|L_{0}\varphi\|_{s}^{2}}&{{}=\sum_{\xi}|P_{l}(\xi)\varphi_{\xi}|^{2}\left(1+|\xi|^{2}\right)^{s}}\\ {}&{{}\geq\operatorname*{c o n s t}\sum_{\xi}|\xi|^{2l}|\varphi_{\xi}|^{2}(1+|\xi|^{2})^{s}.}\\ \end{aligned} $$ 

Hence

(4)

 $$ \begin{aligned}{(\|L_{0}\varphi\|_{s}+\|\varphi\|_{s})^{2}}&{{}\geq\|L_{0}\varphi\|_{s}^{2}+\|\varphi\|_{s}^{2}}\\ {}&{{}\geq\sum_{\xi}|\varphi_{\xi}|^{2}(1+|\xi|^{2})^{s}(1+\operatorname{c o n s t}|\xi|^{2l})}\\ {}&{{}\geq\operatorname{c o n s t}\sum_{\xi}|\varphi_{\xi}|^{2}(1+|\xi|^{2})^{s+l}}\\ {}&{{}=\operatorname{c o n s t}\|\varphi\|_{s+l}^{2}.}\\ \end{aligned} $$ 

Secondly, consider a general periodic elliptic operator $L$ of order $l$, and let $p \in \mathbb{R}^n$. We shall prove that there is a neighborhood $U$ of $p$ such that (1) holds for all $\varphi \in \mathcal{P}$ with support in $U$. (By a slight abuse of terminology we say that the support of a periodic function $\varphi$ lies in $U$ if the support of $\varphi$ lies in the union of $U$ with all of the periodic translates of $U$.) Let $L_0$ denote the constant coefficient elliptic operator, homogeneous of order $l$, determined by the highest-order part of $L$ at the point $p$. Then it follows from (4) that for each $\varphi \in \mathcal{P}$,

 $$ \begin{aligned}{\|\varphi\|_{s+l}}&{{}\leq\mathsf{c o n s t}\left(\|L_{0}\varphi\|_{s}+\|\varphi\|_{s}\right)}\\ {}&{{}\leq\mathsf{c o n s t}\left(\|L\varphi\|_{s}+\|(L_{0}-L)\varphi\|_{s}+\|\varphi\|_{s}\right).}\\ \end{aligned} $$ 

Let $k$ denote the constant in (5). Then choose a positive $\varepsilon$ smaller than $1/(2ck)$, where $c$ denotes the constant $c$ of 6.25. On a small enough neighborhood of $p$ the coefficients of the highest-order part of $L_0-L$ are less than $\varepsilon$ in absolute value. Let $L$ be a periodic operator agreeing with $L_0-L$ on a possibly smaller neighborhood $U$ of $p$ and with coefficients in the highest-order part everywhere less than $\varepsilon$ in absolute value. Then it follows from (5), 6.25(1), and the choice of $\varepsilon$, that for an element $\varphi\in\mathcal{P}$ whose support lies in $U$,

 $$ \begin{aligned}{\|\varphi\|_{s+l}}&{{}\leq\operatorname{c o n s t}\left(\|L\varphi\|_{s}+\|\tilde{L}\varphi\|_{s}+\|\varphi\|_{s}\right)}\\ {}&{{}\leq\operatorname{c o n s t}\|L\varphi\|_{s}+\frac{1}{2}\|\varphi\|_{s+l}+\operatorname{c o n s t}\|\varphi\|_{s+l-1}+\operatorname{c o n s t}\|\varphi\|_{s}.}\\ \end{aligned} $$ 

Applying the Peter-Paul inequality to the term  $ \|\varphi\|_{s+l-1} $, we obtain

 $$ \left\Vert\varphi\right\Vert_{s+1}\leq\mathrm{c o n s t}\left\Vert L\varphi\right\Vert_{s}+\frac{3}{4}\left\Vert\varphi\right\Vert_{s+1}+\mathrm{c o n s t}\left\Vert\varphi\right\Vert_{s}, $$ 

which proves (1) for these φ.

Let  $ T^n $ be the torus obtained as the quotient of  $ \mathbb{R}^n $ by the lattice consisting of all points  $ 2\pi\xi $, where  $ \xi $ is an  $ n $-tuple of integers. The open sets  $ U $ obtained above for each  $ p \in \mathbb{R}^n $ project to an open cover of  $ T^n $. Let  $ U_1, \ldots, U_k $ be a finite subcover, and let  $ \omega_1, \ldots, \omega_k $ be a partition of unity fitting this cover, of the special form

 $$ \sum_{i=1}^{k}\omega_{i}^{2}=1. $$ 

This is easily arranged—see the proofs of 1.11 and 1.10. Now consider the  $ \omega_i $ as periodic  $ C^\infty $ (real-valued) functions on  $ \mathbb{R}^n $. Let  $ \varphi \in \mathcal{P} $. Then by (6), and by 6.18(i) and (j),

 $$ \begin{aligned}{\|\varphi\|_{s+l}^{2}}&{{}=\langle\varphi,\varphi\rangle_{s+l}=\left\langle\sum_{i}\omega_{i}{}^{2}\varphi,\varphi\right\rangle_{s+l}}\\ {}&{{}\leq\sum_{i}\langle\omega_{i}\varphi,\omega_{i}\varphi\rangle_{s+l}+\operatorname{c o n s t}\|\varphi\|_{s+l}\|\varphi\|_{s+l-1}.}\\ \end{aligned} $$ 

Now since $\omega_{i}\varphi$ has support in one of the small open sets $U$ obtained above, and since there are only finitely many of the $\omega_{i}$, there are constants such that the last displayed line above is

\[\begin{aligned}&\leq\mathrm{const}\sum_{i}\|L\omega_{i}\varphi\|_{s}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s+l}\|\varphi\|_{s+l-1}\\&\leq\mathrm{const}\sum_{i}\langle L(\omega_{i}^{\frac{2}{s}}\varphi),L\varphi\rangle_{s}+\mathrm{const}\|\varphi\|_{s}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s+l}\|\varphi\|_{s+l-1}\\&=\mathrm{const}\|L\varphi\|_{s}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s+l}\|\varphi\|_{s+l-1}\tag{by6.27}\\&\leq\mathrm{const}\|\dot{L}\varphi\|_{s}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s}^{\frac{2}{s}}+\frac{1}{2}\|\varphi\|_{s+l}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s+l-1}^{\frac{2}{s}}\\&\leq\mathrm{const}\|L\varphi\|_{s}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s}^{\frac{2}{s}}+\frac{2}{4}\|\varphi\|_{s+l}^{\frac{2}{s}}+\mathrm{const}\|\varphi\|_{s}^{\frac{2}{s}},\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\\&\quad\quad\quad\quad\

It follows that (1) holds for all  $ \varphi \in \mathcal{P} $ and hence for all  $ u \in H_{s+1} $.

6.30 Theorem (Regularity for Periodic Elliptic Operators) Let $L$ be a periodic elliptic operator of order $l$. Assume that $u \in H_{-\infty}, v \in H_{t}$, and

 $$ Lu=v. $$ 

Then  $ u \in H_{t+1} $.

PROOF It is sufficient to prove that if  $ u \in H_s $ and  $ v = Lu \in H_{s-l+1} $, then  $ u \in H_{s+1} $. Let  $ h \in \mathbb{R}^n $ with  $ h \neq 0 $, and let  $ L^h $ represent the operator obtained from  $ L $ by replacing each coefficient  $ \alpha $ by its difference quotient

 $$ \frac{\alpha(x+h)-\alpha(x)}{|h|}. $$ 

Then it follows for  $ \varphi \in \mathcal{P} $, and hence by continuity for all  $ u \in H_{-\infty} $, that

 $$ L(u^{h})=(L u)^{h}-L^{h}(T_{h}u) $$ 

It follows from (2) and the Fundamental Inequality 6.29(1), that

 $$ \begin{aligned}{\|u^{h}\|_{s}}&{{}\leq\operatorname{c o n s t}\|L(u^{h})\|_{s-l}+\operatorname{c o n s t}\|u^{h}\|_{s-l}}\\ {}&{{}\leq\operatorname{c o n s t}\|(L u)^{h}\|_{s-l}+\operatorname{c o n s t}\|L^{h}(T_{h}u)\|_{s-l}+\operatorname{c o n s t}\|u^{h}\|_{s-l}.}\\ \end{aligned} $$ 

Now since the coefficients of the operator L are periodic  $ C^{\infty} $ functions, their difference quotients are uniformly bounded, so that

 $$ \|L^{h}(T_{h}u)\|_{s-l}\leq\mathrm{c o n s t}\|T_{h}(u)\|_{s} $$ 

where the constant does not depend on h. It follows from (3), (4), and 6.19(3) and (5) that

 $$ \left\Vert{u^{h}}\right\Vert_{s}\leq\mathrm{c o n s t}\left\Vert{L u}\right\Vert_{s-l+1}+\mathrm{c o n s t}\left\Vert{u}\right\Vert_{s}, $$ 

where the right-hand side is independent of $h$. Thus, by $6.20$, $u \in H_{s+1}$, and the theorem is proved.

##### REDUCTION TO THE PERIODIC CASE

6.31 Remarks Before beginning the proof of Theorem 6.5 we need to establish some convenient notation and to make a few observations.

We are going to let $C^{\infty}$ denote the set of all complex $m$-space valued $C^{\infty}$ functions on $\mathbb{R}^n$. $C_0^{\infty}$ will denote those of compact support, and $C_0^{\infty}(V)$ those whose compact support lies in $V$. By the $L_2$ inner product on $C_0^{\infty}$ we shall mean

 $$ \langle u,v\rangle=\frac{1}{(2\pi)^{n}}\int_{R^{n}}u\cdot v, $$ 

where  $ u \cdot v $ as before denotes the Hermitian product  $ u_1\overline{v_1} + \cdots + u_m\overline{v_m} $.

Let $V$ be an open set in $\mathbb{R}^n$ with $\overline{V}$ contained in some $2\pi$ cube. Then by extending periodically we can (and do) identify $C_0^\infty(V)$ with a subspace of $\mathcal{P}$. Observe that the $L_2$ inner product on $C_0^\infty(V)$ agrees with the $L_2$ inner product on $C_0^\infty(V)$ considered as a subset of $\mathcal{P}$, which in turn agrees with the Sobolev inner product $\|\cdot\|_0$.

Now suppose that $L$ is an elliptic partial differential operator of order $l$ on $C^\infty$ (no assumption of periodic coefficients). $L$ has a formal adjoint $L^*$ on $C_0^\infty$, with respect to the ordinary $L_2$ inner product on $C_0^\infty$, obtained by integration by parts. Just as in 6.24, if $L = (L_{ij})$ where $L_{ij} = \sum a_i^e D^e$, then $L^* = (L_{ij}^*)$ where $L_{ij}^* = \sum D^e a_{ji}^e$. $L^*$ is also a differential operator of order $l$.

Now let $p \in \mathbb{R}^n$. Then there is a sufficiently small neighborhood $V$ of $p$ and a periodic elliptic operator $L$ such that $L$ agrees with $L$ on $V$. For let $L_0$ denote the constant coefficient operator determined by $L$ at $p$. Then since $L$ is elliptic at $p$, there is some $\varepsilon > 0$ such that any operator whose coefficients are everywhere within $\varepsilon$ in absolute value of the corresponding coefficients of $L_0$ is elliptic. So let $U$ be a neighborhood of $p$, small enough to be contained in some $2\pi$ cube $Q$, on which the coefficients of $L$ differ from the corresponding coefficients of $L_0$ by at most $\varepsilon$; and let $V \subset \overline{V} \subset U$. Choose a $C^\infty$ function $\varphi$ with $0 \leq \varphi \leq 1$ such that $\varphi$ is 1 on $V$ and has support in $U$. Then the operator

 $$ \varphi\cdot L+(1-\varphi)L_{0} $$ 

is elliptic on all of  $ \mathbb{R}^n $ and clearly can be extended from Q to be a periodic elliptic operator L which agrees with L on V.

We shall need the following slight extension of the formal adjoint property of  $ L^* $. Let  $ u \in H_s $, and let  $ \varphi \in C_0^\infty(V) $. Then

 $$ \langle\mathcal{I}u,\varphi\rangle_{0}=\langle u,L^{*}\varphi\rangle_{0}. $$ 

For let  $ \psi_{j} \to u $ in  $ \| \| $, with  $ \psi_{j} \in \mathcal{P} $. Then

 $$ \begin{aligned}{\langle\widetilde{L}\psi_{j},\varphi\rangle_{0}}&{{}=\langle\widetilde{L}\psi_{j},\varphi\rangle=\langle L\psi_{j},\varphi\rangle}\\ {}&{{}=\langle\psi_{j},L^{*}\varphi\rangle=\langle\psi_{j},L^{*}\varphi\rangle_{0},}\\ \end{aligned} $$ 

so that

 $$ \begin{aligned}{|\langle\widetilde{L}u,\varphi\rangle_{0}-\langle u,L^{*}\varphi\rangle_{0}|}&{{}=|\langle\widetilde{L}(u-\psi_{j}),\varphi\rangle_{0}-\langle u-\psi_{j},L^{*}\varphi\rangle_{0}|}\\ {}&{{}\leq\|\widetilde{L}(u-\psi_{j})\|_{s-l}\|\varphi\|_{-s+l}+\|u-\psi_{j}\|_{s}\|L^{*}\varphi\|_{-s}}\\ {}&{{}\leq\operatorname{c o n s t}\|u-\psi_{j}\|_{s}\|\varphi\|_{-s+l}+\|u-\psi_{j}\|_{s}\|L^{*}\varphi\|_{-s},}\\ \end{aligned} $$ 

which converges to zero as  $ j \to \infty $.

Let $V$, as above, be an open set whose closure lies in some $2\pi$ cube. Let $u$ and $v$ belong to $H_{s}$. Then we shall say that $u$ and $v$ are equal on $V$ if

 $$ \langle u-v,\varphi\rangle_{0}=0 $$ 

for all $\varphi \in C_0^\infty(V)$. We shall say that a periodic operator $L$ has support in $V$ if the coefficients of $L$ belong to $C_0^\infty(V) \subset \mathcal{P}$. Now, if $L$ has support in $V$, and if the elements $u$ and $v$ of $H_s$ are equal on $V$, then

 $$ L u=L v. $$ 

For by 6.18(f), it is sufficient to prove that

 $$ \langle L(u-v),\varphi\rangle_{0}=0 $$ 

for all $\varphi \in \mathcal{P}$. But applying (2) (with $\tilde{L} = L$), we obtain

 $$ \langle L(u-v),\varphi\rangle_{0}=\langle(u-v),L^{*}\varphi\rangle_{0} $$ 

which is zero by (3) since  $ L^{*}\varphi\in C_{0}^{\infty}(V)\subset\mathcal{P} $.

6.32 Proof of the Regularity Theorem 6.5 We are going to restate Theorem 6.5 in slightly different notation, adapted to the local problem in  $ \mathbb{R}^{n} $ to which the theorem will immediately be reduced. We shall use  $ \langle $,  $ \rangle $ to denote the inner product 6.1(5) on  $ E^{p}(M) $. We shall prove:

(1) Given a $C^\infty$ p-form for $M$ and a bounded linear functional $l^\prime$: $E^p(M) \to \mathbb{R}$ such that $l^\prime(\Delta^* \phi) = \langle f, \phi \rangle^\prime$ for every $\phi \in E^p(M)$, then there exists a $C^\infty$ p-form $u$ on $M$ such that $l^\prime(t) = \langle u, t \rangle^\prime$ for every $t \in E^p(M)$.

We note that the last statement of Theorem 6.5, which says that $\Delta u = f$, is an immediate consequence of (1), since, as we have already observed in 6.4(6), $\langle\Delta u,\varphi\rangle' = \langle u,\Delta^*\varphi\rangle' = l'(\Delta^*\varphi) = \langle f,\varphi\rangle'$ for all $\varphi \in E^p(M)$.

We now reduce Theorem 6.5 to a local problem. Let $U$ be a coordinate patch on $M$ with coordinate map $\gamma$ such that $\gamma(U) = \mathbb{R}^n$. Via this coordinate system, differentiable $p$-forms become vector-valued functions from $\mathbb{R}^n$ to $\mathbb{R}^m \subset \mathbb{C}^m$ where $m = \binom{n}{p}$. We adopt the notation of 6.31. So via the coordinate system $(U,\gamma)$, $p$-forms on $M$ yield elements of $C^\infty$; and in the reverse direction, each element of $C^\infty$ extends by zero to a complex-valued $p$-form on all of $M$. The Laplacian $\Delta$ induces a partial differential operator $L$ of order 2 on $C^\infty$. The basic fact that we shall need concerning $L$ is that $L$ is an elliptic operator. This we assume for the moment and shall establish in 6.35. We let $L^*$ denote the formal adjoint of $L$ with respect to the $L_2$ inner product on $C_0^\infty$.

We extend the inner product  $ \langle\cdot,\rangle' $ to complex-valued p-forms in the obvious way, so that if  $ u_{1}, u_{2}, v_{1} $, and  $ v_{2} $ are real-valued p-forms, then

 $$ \langle u_{1}+i u_{2},v_{1}+i v_{2}\rangle^{\prime}=\langle u_{1},v_{1}\rangle^{\prime}+\langle u_{2},v_{2}\rangle^{\prime}+i(\langle u_{2},v_{1}\rangle^{\prime}-\langle u_{1},v_{2}\rangle^{\prime}). $$ 

Then by transferring this to Euclidean space we obtain another inner product  $ \langle $,  $ \rangle $ on  $ C_{0}^{\infty} $ induced from the inner product on complex-valued p-forms on M. It follows from the observation that both the  $ L_{2} $ inner product  $ \langle $,  $ \rangle $ and the inner product  $ \langle $,  $ \rangle $ on  $ C_{0}^{\infty} $ are integrals of pointwise inner products, that there exists a matrix A of smooth functions on  $ R^{n} $, Hermitian and positive definite at each point, such that

 $$ \langle\varphi,\psi\rangle^{\prime}=\langle\varphi,A\psi\rangle $$ 

for all  $ \varphi, \psi \in C_0^\infty $.

The adjoint of $L$ on $C_0^\infty$ with respect to $\langle \ , \rangle' $ is simply $\Delta^*$ restricted to $C_0^\infty$. We claim that for $\varphi \in C_0^\infty$,

 $$ {\cal L}^{*}\varphi=A\Delta^{*}A^{-1}\varphi. $$ 

Indeed, for arbitrary  $ \psi \in C_{0}^{\infty} $,

 $$ \begin{aligned}{\langle L^{*}\varphi,\psi\rangle}&{{}=\langle\varphi,L\psi\rangle=\langle A^{-1}\varphi,L\psi\rangle^{\prime}}\\ {}&{{}=\langle\Delta^{*}A^{-1}\varphi,\psi\rangle^{\prime}=\langle A\Delta^{*}A^{-1}\varphi,\psi\rangle.}\\ \end{aligned} $$ 

We extend the linear functional $l': E^p(M) \to \mathbb{R}$ complex linearly to complex-valued differential forms, and we define a complex-valued linear functional $l$ on $C_0^\infty$ by setting

 $$ I(\varphi)=I^{\prime}(A^{-1}\varphi). $$ 

We claim that $l$ is locally represented by a $C^{\infty}$ function. Precisely, we shall prove:

(5) If $p \in \mathbb{R}^n$, then there is a neighborhood $W_p$ of $p$ and an element $u_p \in \mathcal{P}$ such that $l(t) = \langle u_p, t \rangle$ for every $t \in C_0^\infty(W_p)$.

First we show that (5) implies (1). It follows from (5) that for each $p, q \in \mathbb{R}^n$, $u_p \mid W_p \cap W_q = u_q \mid W_p \cap W_q$, since both $u_p$ and $u_q$ have the same $L_2$ inner product with all elements of $C_0^w(W_p \cap W_q)$. Thus the $u_p$ piece together to give $u \in C^\infty$ such that $u \mid W_p = u_p \mid W_p$ for each $p \in \mathbb{R}^n$. Now let $\{\varphi_i\}$ be a partition of unity on $\mathbb{R}^n$ subordinate to the $\{W_p\}$. Then if $t \in C_0^\infty$, $l(t) = \sum_i l(\varphi_i t) = \sum_i \langle u, \varphi_i t \rangle = \langle u, t \rangle$. Now if $\varphi$ is a smooth $p$-form on $M$ with support in $U$, then $l'(\varphi) = l(A\varphi) = \langle u, A\varphi \rangle = \langle u, \varphi \rangle$. By the same argument as above, the $u$'s for various coordinate systems on $M$ piece together to form a $C^\infty$ $p$-form $u$ (necessarily real-valued) on $M$ such that $l'(\varphi) = \langle u, \varphi \rangle$ for every $\varphi \in E^p(M)$. Thus we have reduced the proof of (1) to the proof of (5), which follows.

Let $p \in \mathbb{R}^n$ be fixed, and let $Q'$ be some open $2\pi$ cube containing $p$. Choose an open set $V$ such that $p \in V \subset \overline{V} \subset Q'$, and let

 $$ \tilde{l}=l\mid C_{0}^{\infty}(V). $$ 

First of all, we observe that  $ \tilde{I} $ is a bounded linear functional on  $ C_0^\infty(V) $. For since  $ \overline{V} $ is compact, the matrix norms  $ \|A_a^{-1}\| $ have a maximum as x ranges over  $ \overline{V} $, and thus, using the fact that  $ I' $ is bounded, we obtain

 $$ \begin{aligned}{|\tilde{l}(\varphi)|}&{{}=|l(\varphi)|=|l^{\prime}(A^{-1}\varphi)|\leq\operatorname{c o n s t}\|A^{-1}\varphi\|^{\prime}}\\ {}&{{}=\operatorname{c o n s t}\left(\langle A^{-1}\varphi,A^{-1}\varphi\rangle^{\prime}\right)^{1/2}=\operatorname{c o n s t}\langle\varphi,A^{-1}\varphi\rangle^{1/2}}\\ {}&{{}\leq\operatorname{c o n s t}\left(\|\varphi\|\|A^{-1}\varphi\|\right)^{1/2}\leq\operatorname{c o n s t}\|\varphi\|}\\ \end{aligned} $$ 

for all  $ \varphi \in C_0^\infty(V) $. Second, we observe that it follows from (6), (4), (3), (2), and (1) that

 $$ \tilde{l}(L^{*}\varphi)=l^{\prime}(A^{-1}L^{*}\varphi)=l^{\prime}(\Delta^{*}A^{-1}\varphi)=\langle f,A^{-1}\varphi\rangle^{\prime}=\langle f,\varphi\rangle $$ 

for all  $ \varphi \in C_{0}^{\infty}(V) $. Thus  $ \tilde{l} $ is a weak solution of  $ Lu = f $.

Since $\tilde{l}$ is bounded, $\tilde{l}$ extends to a bounded linear functional on $H_0$. It follows that there is an element $\tilde{u} \in H_0$ such that

(8)

 $$ \tilde{l}(t)=\langle\tilde{u},t\rangle_{0}\quad\mathrm{f o r~a l l~}t\in H_{0}. $$ 

Our task is to show that on a small enough neighborhood of $p$, the element $\tilde{u}$ agrees with an element of $\mathcal{P}$.

Choose a neighborhood $O_{0}$ of $p$ with $\overline{O_{0}} \subset V$ small enough so that there exists a periodic elliptic operator $\widetilde{L}$ which agrees with $L$ on $O_{0}$ (cf. 6.31). Choose a neighborhood $O$ of $p$ such that $\overline{O} \subset O_{0}$, and then choose a sequence

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl-16-online//fa06cdba-fa45-445f-af46-dfae42077371/markdown_2/imgs/img_in_image_box_490_419_808_707.jpg?authorization=bce-auth-v1%2FALTAKDN8mY5KlNI7zaRpLmOqrw%2F2026-08-12T12%3A05%3A17Z%2F-1%2F%2F459664f837b9100750613cf53e77f579efaf1c49f98a3507266ccb018bf6bfe8" alt="Image" width="33%" /></div>

of neighborhoods $O_n$ of $p$ such that $\overline{O} \subset O_n$ and $\overline{O_n} \subset O_{n-1}$ for each $n=1,2,\ldots$. For each integer $n\geq1$, choose a $C^\infty$ function $\omega_n$ which is identically equal to 1 on $O_n$, has values between 0 and 1, and has support in $O_{n-1}$. Let

(9)

 $$ v_{1}=\omega_{1}\tilde{u}\in H_{0}. $$ 

Then

 $$ \begin{array}{r}{\tilde{L}\boldsymbol{v}_{1}=\tilde{L}\omega_{1}\tilde{\boldsymbol{u}}=\omega_{1}\tilde{L}\tilde{\boldsymbol{u}}+\boldsymbol{M}_{1}\tilde{\boldsymbol{u}},}\end{array} $$ 

where

 $$ \begin{array}{r}{M_{1}=\tilde{L}\omega_{1}-\omega_{1}\tilde{L}.}\end{array} $$ 

In order to apply 6.30, we must first determine to which Sobolev space the right-hand side of (10) belongs.

First, we claim that

(12)

 $$ \omega_{1}\tilde{L}\tilde{u}=\omega_{1}f, $$ 

from which it follows that  $ \omega_1\tilde{L}\tilde{u} \in C_0^\infty(O_0) $ and thus belongs to  $ H_s $ for each  $ s $. Now both sides of (12) belong to some  $ H_s $, and it follows from 6.18(f) that for (12) to hold, it is sufficient to prove that

 $$ \langle\omega_{1}\tilde{L}\tilde{u}-\omega_{1}f,\varphi\rangle_{0}=0 $$ 

for all  $ \varphi \in \mathcal{P} $. We compute, using (7), (8), 6.18(9), and 6.31(2):

 $$ \begin{aligned}{\langle\omega_{1}\widetilde{L}\widetilde{u}-\omega_{1}f,\varphi\rangle_{0}}&{{}=\langle\omega_{1}\widetilde{L}\widetilde{u},\varphi\rangle_{0}-\langle\omega_{1}f,\varphi\rangle_{0}}\\ {}&{{}=\langle\widetilde{L}\widetilde{u},\omega_{1}\varphi\rangle_{0}-\langle f,\omega_{1}\varphi\rangle_{0}}\\ {}&{{}=\langle\widetilde{u},L^{*}\omega_{1}\varphi\rangle_{0}-\widetilde{l}(L^{*}\omega_{1}\varphi)}\\ {}&{{}=\widetilde{l}(L^{*}\omega_{1}\varphi)-\widetilde{l}(L^{*}\omega_{1}\varphi)=0.}\\ \end{aligned} $$ 

Thus (12) holds. Now since $L$ (and hence $\tilde{L}$) is an operator of order 2, then $M_1$ is of order 1; hence $M_1\tilde{u} \in H_{-1}$. Thus the right-hand side of (10) belongs to $H_{-1}$. It follows from the periodic regularity theorem 6.30 that $v_1 \in H_1$. Now we let

 $$ v_{2}=\omega_{2}\tilde{u}. $$ 

Then

 $$ \begin{array}{r}{\tilde{L}\boldsymbol{v}_{\mathbf{z}}=\omega_{\mathbf{z}}\tilde{L}\tilde{\boldsymbol{u}}+\boldsymbol{M}_{\mathbf{z}}\tilde{\boldsymbol{u}}=\omega_{\mathbf{z}}\tilde{L}\tilde{\boldsymbol{u}}+\boldsymbol{M}_{\mathbf{z}}\boldsymbol{v}_{\mathbf{1}},}\end{array} $$ 

where the last equality follows from 6.31(4) since  $ M_2 = \tilde{L}\omega_2 - \omega_2\tilde{L} $ has support in  $ O_1 $ and  $ \tilde{u} = v_1 $ on  $ O_1 $. Now, arguing as before, we see that the right-hand side of (15) lies in  $ H_0 $. Thus by 6.30,  $ v_2 \in H_2 $. Continuing in the same manner, we obtain

 $$ v_{n}=\omega_{n}\tilde{u}\quad\mathrm{w i t h}v_{n}\in H_{n}. $$ 

Finally, let $W_p$ be an open neighborhood of $p$ with $\overline{W}_p \subset O$, and let $\omega$ be identically 1 on $W_p$ with values between 0 and 1, and with support in $O$. Then $\omega\tilde{u} = \omega\omega_n\tilde{u}$ for each $n$; and so by (16), $\omega\tilde{u} \in H_n$ for every $n$. By the corollary to the Sobolev lemma 6.22, $\omega\tilde{u}$ represents a $C^\infty$ function $u \in \mathcal{P}$. Now if $t \in C_0^\infty(W_p)$, then

 $$ \begin{aligned}{l(t)}&{{}=\tilde{l}(t)=\langle\tilde{u},t\rangle_{0}=\langle\tilde{u},\omega t\rangle_{0}}\\ {}&{{}=\langle\omega\tilde{u},t\rangle_{0}=\langle u,t\rangle,}\\ \end{aligned} $$ 

and (5) is proved. Except for a proof of the fact that $L$ is elliptic, this completes the proof of Theorem 6.5.

6.33 Proof of Theorem 6.6 It suffices to show that if $m \in M$, then there is some neighborhood of $m$ such that if $\varphi$ is any $C^\infty$ function on $M$ with support in that neighborhood, then $\{\varphi\alpha_n\}$ has a Cauchy subsequence. For then we simply cover $M$ by a finite number of such neighborhoods

and take a partition of unity $\varphi_{1},\ldots,\varphi_{N}$ subordinate to this cover. One can select a subsequence $\alpha_{n_{k}}$ such that $\varphi_{j}\alpha_{n_{k}}$ is Cauchy for each $j$. Then $\{\alpha_{n_{k}}\}$ is Cauchy for

 $$ \begin{array}{r l}{\|\alpha_{n_{k}}-\alpha_{n_{1}}\|=\Big\|\underset{j=1}{\overset{N}{\sum}}\varphi_{j}(\alpha_{n_{k}}-\alpha_{n_{1}})\Big\|}&{\leq\quad\underset{j=1}{\overset{N}{\sum}}\|\varphi_{j}\alpha_{n_{k}}-\varphi_{j}\alpha_{n_{1}}\|.}\end{array} $$ 

We reduce the problem to Euclidean space by choosing a coordinate neighborhood of $m$ with $m$ going to $p \in \mathbb{R}^n$. We continue with the notation and setup as developed in 6.31 and 6.32; in particular, the norm on $M$ and the corresponding induced norm on $C_0^\infty$ will now be denoted by $\| \cdot \|$. Let $\varphi$ be a real-valued $C^\infty$ function with support in $O_0$. It suffices to show that the sequence $\{\varphi_{\alpha_n}\}$ of elements of $\mathcal{P}$ has a Cauchy subsequence $\{\varphi_{\alpha_n}\}$ in the 0-norm, since the 0-norm and the $L_2$-norm agree on $C_0^\infty(O_0)$, and the $L_2$-norm and the norm $\| \cdot \|$ are equivalent on $C_0^\infty(O_0)$. According to the Rellich lemma 6.23, in order to prove that $\{\varphi_{\alpha_n}\}$ has a Cauchy subsequence in the 0-norm, it is sufficient to show that the sequence is bounded in $H_1$. It follows from the Fundamental Inequality that

 $$ \begin{aligned}{\|\varphi\alpha_{n}\|_{1}}&{{}\leq\operatorname{c o n s t}\left(\|\widetilde{L}\varphi\alpha_{n}\|_{-1}+\|\varphi\alpha_{n}\|_{-1}\right)}\\ {}&{{}=\operatorname{c o n s t}\left(\|L\varphi\alpha_{n}\|_{-1}+\|\varphi\alpha_{n}\|_{-1}\right)}\\ {}&{{}\leq\operatorname{c o n s t}\|\varphi L\alpha_{n}\|_{-1}+\operatorname{c o n s t}\|(L\varphi-\varphi L)\alpha_{n}\|_{-1}+\operatorname{c o n s t}\|\varphi\alpha_{n}\|_{-1}.}\\ \end{aligned} $$ 

Now

 $$ \begin{aligned}{\|\varphi L\alpha_{n}\|_{-1}}&{{}\leq\|\varphi L\alpha_{n}\|_{0}=\|\varphi L\alpha_{n}\|}\\ {}&{{}\leq\operatorname{c o n s t}\|\varphi L\alpha_{n}\|^{\prime}\leq\operatorname{c o n s t}\|L\alpha_{n}\|^{\prime}\leq\operatorname{c o n s t}\|\Delta\alpha_{n}\|^{\prime}.}\\ \end{aligned} $$ 

Let  $ \tau $ be a  $ C^{\infty} $ function with values between 0 and 1 which equals 1 on  $ O_{0} $ and has support in V. Then

 $$ (L_{\varphi}-\varphi L)\alpha_{n}=(L\varphi-\varphi L)(\tau\alpha_{n}), $$ 

so that

 $$ \begin{aligned}{\|(L\varphi-\varphi L)\alpha_{n}\|_{-1}}&{{}=\|(L\varphi-\varphi L)(\tau\alpha_{n})\|_{-1}}\\ {}&{{}\leq\operatorname{c o n s t}\|\tau\alpha_{n}\|_{0}=\operatorname{c o n s t}\|\tau\alpha_{n}\|}\\ {}&{{}\leq\operatorname{c o n s t}\|\tau\alpha_{n}\|^{\prime}\leq\operatorname{c o n s t}\|\alpha_{n}\|^{\prime}.}\\ \end{aligned} $$ 

Finally,

 $$ \begin{array}{r}{\|\varphi\alpha_{n}\|_{-1}\leq\|\varphi\alpha_{n}\|_{0}=\|\varphi\alpha_{n}\|\leq\mathrm{c o n s t}\|\varphi\alpha_{n}\|^{\prime}\leq\mathrm{c o n s t}\|\alpha_{n}\|^{\prime}.}\end{array} $$ 

So from (1), (2), (3), and (4) we obtain

 $$ \|\varphi\alpha_{n}\|_{1}\leq\mathrm{c o n s t}\left(\|\Delta\alpha_{n}\|^{\prime}+\|\alpha_{n}\|^{\prime}\right). $$ 

But by assumption $\|\Delta\alpha_n\|' $ and $\|\alpha_n\|' $ are bounded. Therefore, the sequence $\{\varphi\alpha_n\}$ is bounded in $H_1$, and the proof of Theorem 6.6 is complete (assuming the ellipticity of $L$).

#### ELLIPTICITY OF THE LAPLACE-BELTRAMI OPERATOR

6.34 Remark We shall make use of the following observation. Let $U$, $V$, and $W$ be finite dimensional inner product spaces, and suppose that

 $$ U\mathop{\longrightarrow}\limits^{\mathbf{A}}\vphantom{\int}V\mathop{\longrightarrow}\limits^{\mathbf{B}}\vphantom{W}\rightarrow W $$ 

is exact. Let $A^{*}\colon V\to U$ and $B^{*}\colon W\to V$ be the adjoints of $A$ and $B$ respectively. Then $B^{*}B+AA^{*}$ is an isomorphism on $V$. For let $v$ be a non-zero element of $V$. We need only show that $(B^{*}B+AA^{*})v\neq0$. Now

 $$ \langle(B^{*}B+A A^{*})v,v\rangle=\langle B v,B v\rangle+\langle A^{*}v,A^{*}v\rangle. $$ 

If $Bv \neq 0$, then $(B^*B + AA^*)v \neq 0$. If $Bv = 0$, then by the exactness, $v$ lies in the image of $A$. But $A^*$ is injective on the image of $A$. Thus $A^*v \neq 0$, which implies that $(B^*B + AA^*)v \neq 0$.

We shall apply this to the special case in which $U$, $V$, and $W$ are $\Lambda_{p-1}(M_{m}^{*}), \Lambda_{p}(M_{m}^{*})$, and $\Lambda_{p+1}(M_{m}^{*})$ respectively, with the inner products

 $$ \langle\omega,\tau\rangle=\ast(\omega\wedge\ast\tau), $$ 

and with $A$ and $B$ both left exterior multiplication by $\xi \in M_{m}^{*}$:

 $$ \Lambda_{p-1}(M_{m}^{*})\xrightarrow{\xi}\Lambda_{p}(M_{m}^{*})\xrightarrow{\xi}\Lambda_{p+1}(M_{m}^{*}). $$ 

According to Exercise 15 of Chapter 2, the sequence (1) is exact; and according to Exercise 14 of Chapter 2, the adjoint of  $ \xi\colon \Lambda_{p}(M_{m}^{*})\to\Lambda_{p+1}(M_{m}^{*}) $ is

 $$ (-1)^{n p}*{\xi}*:\:\Lambda_{p+1}(M_{m}^{*})\to\Lambda_{p}(M_{m}^{*}). $$ 

Thus it follows from the above remarks that

 $$ (-1)^{n p}{*}\xi{*}\xi+(-1)^{n(p-1)}\xi{*}\xi{*} $$ 

is an isomorphism on  $ \Lambda_{p}(M_{m}^{*}) $.

6.35 The Laplacian is Elliptic. In order to complete the proofs of Theorems 6.5 and 6.6, we need to prove that the operator $L$ of 6.32 induced on Euclidean space by the Laplace-Beltrami operator $\Delta$ via a coordinate system is elliptic. Proving this, according to 6.28(2), is equivalent to showing that for each $m \in M$,

 $$ \Delta(\varphi^{2}\alpha)(m)\neq0 $$ 

for each smooth form $\alpha$ such that $\alpha(m) \neq 0$ and for each $C^\infty$ function $\varphi$ on $M$ such that $\varphi(m) = 0$ but $d\varphi(m) \neq 0$. Assume that $\alpha$ is a $p$-form, and let $0 \neq d\varphi = \xi \in M_m^*$. Recall that

 $$ \Delta=(-1)^{n(\mathfrak{p}+1)+1}d{*}d{*}+(-1)^{n\mathfrak{p}+1}{*}d{*}d{.} $$ 

We compute the left-hand side of (1), keeping in mind at each stage that  $ \varphi(m) = 0 $. Thus

 $$ \begin{aligned}{d{*}d{*}(\varphi^{\sharp}\alpha)(m)}&{{}=\big(d{*}d(\varphi^{\sharp}){*}\alpha\big)(m)=\big(2d{*}\varphi(d\varphi){*}\alpha\big)(m)}\\ {}&{{}=\big(2(d\varphi){*}(d\varphi){*}\alpha\big)(m)=2\xi{*}\xi{*}\big(\alpha(m)\big).}\\ \end{aligned} $$ 

Similarly,

 $$ *d*d(\varphi^{8}\alpha)(m)=2*\xi*\xi\bigl(\alpha(m)\bigr). $$ 

Thus

 $$ \Delta(\varphi^{2}\alpha)(m)=-2[(-1)^{n p}\ast\xi\ast\xi+(-1)^{n(p-1)}\xi\ast\xi\ast]\bigl(\alpha(m)\bigr), $$ 

which is not zero, according to 6.34(3). Hence  $ \Delta $ is elliptic, and the proof of the Hodge theorem is at last complete.

6.36 Remark We have seen that for each $\xi$ in $M_m^*$ there is a well-defined linear transformation $\sigma_\Delta(\xi)$ on $\Lambda_p(M_m^*)$ defined by

 $$ \sigma_{\Delta}(\xi)(v)=\Delta(\varphi^{\sharp}\alpha)(m), $$ 

where  $ v \in \Lambda_p(M_m^*) $, where  $ \alpha $ is any  $ p $-form such that  $ \alpha(m) = v $, and where  $ \varphi $ is any  $ C^\infty $ function such that  $ \varphi(m) = 0 $ and  $ d\varphi(m) = \xi $. This linear transformation  $ \sigma_\Delta(\xi) $ is known as the symbol of the operator  $ \Delta $. The ellipticity of all the operators  $ L $ on  $ \mathbb{R}^n $ obtained from  $ \Delta $ via coordinate systems is equivalent to the property that the symbol  $ \sigma_\Delta(\xi) $ is an isomorphism at each point  $ m $ for each non-zero  $ \xi \in M_m^* $. Our computations in 6.35 contain a proof of the fact that the symbol of the exterior derivative operator  $ d $, namely  $ \sigma_d(\xi): \Lambda(M_m^*) \to \Lambda(M_m^*) $, is simply left exterior multiplication by  $ \xi $; whereas the symbol of the adjoint  $ \delta $ of  $ d $ is the adjoint of left exterior multiplication by  $ \xi $. In the theory of general partial differential operators on vector bundles over  $ M $, ellipticity is defined, as above, in terms of the symbol.

##### EXERCISES

1 Prove that  $ *\Delta = \Delta* $.

2 (a) Prove that the Green's operator G is a bounded linear operator.

(b) Prove that $G$ is self-adjoint on $(H^{p})^{\perp}$.

(c) Prove that G takes bounded sequences into sequences with Cauchy subsequences.

3 By using an integral test, prove that the series  $ \sum(1 + |\xi|^{\sharp})^{-k} $, where  $ \xi $ ranges over all  $ n $-tuples of integers  $ (\xi_1, \ldots, \xi_n) $, converges for  $ k \geq [n/2] + 1 $. (Hint: Induct on  $ n $, and evaluate the appropriate integrals in terms of spherical coordinates.)

4 Prove in detail the inequality 6.16(15).

5 Establish the existence of the matrix A of 6.32(2) together with its stated properties.

6 Derive explicit formulas for $d, \ast, \delta$, and $\Delta$ in Euclidean space. In particular, show that if

 $$ \alpha=\sum_{i_{1}<\cdots<i_{p}}\alpha_{I}\;d x_{i_{1}}\wedge\cdots\wedge d x_{i_{p}}, $$ 

then

 $$ \Delta\alpha=(-1)\sum_{i_{1}<\cdots<i_{p}}\left(\sum_{i=1}^{n}\frac{\partial^{2}\alpha_{I}}{\partial x_{i}^{2}}\right)\;d x_{i_{1}}\wedge\cdots\wedge d x_{i_{p}}. $$ 

7 Let  $ \varphi $ belong to the  $ C^{\infty} $ periodic functions  $ \mathcal{P} $ on the plane. Prove that

 $$ \left\|\frac{\partial^{2}\varphi}{\partial x\partial y}\right\|\leq\frac{1}{\varepsilon}\left\|\Delta\varphi\right\|. $$ 

8 The Rellich lemma 6.23 says that the natural injection $i: H_{t} \to H_{s}$ for $s < t$ is a compact operator; that is, it takes bounded sequences into sequences with convergent subsequences. An analogous example of this phenomenon is the following. Let $C$ denote the Banach space of periodic continuous functions on the real line, say with period $2\pi$, and with norm the sup norm $\|\cdot\|_{\infty}$. Let $C^{1}$ be the subset of $C$ consisting of functions with continuous first derivative. As a norm for $C^{1}$ we take

 $$ \left\|f\right\|=\left\|f\right\|_{\infty}+\left\|\frac{d f}{d x}\right\|_{\infty}. $$ 

Use the Arzelà-Ascoli theorem [27, p. 126] to prove that the natural injection $i\colon C^{1}\to C$ is a compact operator.

9 We shall consider a number of elliptic equations of the form $Lu = f$ on the real line. In each case, $f$ will be smooth and periodic of period 1, and we look for solutions $u$ also periodic of period 1. This restriction to periodic functions makes this in essence a problem on a compact space, the unit circle. We let $u' = du/dx$. etc.

(a)  $ u' = f $. This is the simplest example of an elliptic operator which exhibits all of the essential ingredients of the theory. What is the formal adjoint of this differential operator? Show that there is a solution u (periodic) if and only if f is orthogonal to the kernel of this adjoint.

(b)  $ u^{\prime}-u=f $. What is the kernel (in the periodic functions) in this case? What are the necessary and sufficient conditions on f for there to exist a periodic solution?

(c) $u'' = f$. Show that this operator is formally self-adjoint. Show that there is a periodic solution if and only if $f$ is orthogonal to the kernel; and using the fact that

 $$ \int_{0}^{\infty}\left(\int_{0}^{t}f(s)ds\right)dt=\int_{0}^{\infty}f(s)\left(\int_{s}^{\infty}dt\right)ds, $$ 

show that the unique solution orthogonal to the kernel is

 $$ \begin{aligned}{u(x)=}&{{}\int_{0}^{\varepsilon}t(x-1)f(t)\mathop{}{d}t\quad+\quad\int_{\varepsilon}^{1}x(t-1)f(t)\mathop{}{d}t}\\ {}&{{}+\frac{1}{2}\int_{0}^{1}t(t-1)f(t)\mathop{}{d}t.}\\ \end{aligned} $$ 

This explicitly exhibits the Green's operator for this case.

(d)  $ u'' + \pi^u = f $. Show that this operator is formally self-adjoint. What is its kernel? Derive an explicit formula for the solution u, and show that u is periodic if and only if f is orthogonal to the kernel.

10 In Theorem 6.11 we used the fact that the Green's operator commutes with $d$ in proving that each closed form on a compact orientable Riemannian manifold differs from a harmonic form by an exact form. Give a proof of this result directly from the Hodge decomposition theorem without using the Green's operator.

11 A periodic distribution $l$ is a linear functional on $\mathcal{P}$ for which there exists some integer $k \geq 0$ and a positive constant $c$ such that

 $$ |l(\varphi)|\leq c\sum_{|\alpha|\leq k}\|D^{\alpha}\varphi\|_{\infty} $$ 

for all $\varphi \in \mathcal{P}$. Prove that if $l$ is a periodic distribution, then there is an element $u \in H_{-\infty}$ such that

 $$ l(\varphi)=\langle u,\varphi\rangle_{0} $$ 

for all $\varphi \in \mathcal{P}$. Conversely show that every element of $H_{-\infty}$ determines a periodic distribution via (2).

12 Let  $ \alpha $ and  $ \beta $ be n-forms on a compact oriented manifold  $ M^n $ such that  $ \int_M \alpha = \int_M \beta $. Prove that  $ \alpha $ and  $ \beta $ differ by an exact form.

13 Show that Theorem 6.6 cannot be strengthened to the assertion of the existence of a subsequence which is convergent in  $ E^{p}(M) $.

14 One should observe that in the course of proving Theorem 6.5 we have proved the following regularity theorem. Let $L$ be an elliptic operator on $C^\infty$ (the complex $m$-space valued smooth functions on $\mathbb{R}^n$). Suppose that $u$ is sufficiently differentiable for $Lu$ to make sense, and suppose that $Lu = f$ where $f \in C^\infty$. Then $u \in C^\infty$.

In fact, we have proved more—every weak solution $l$ is smooth. Precisely: Let $l$ be a linear functional on $C_0^\infty$ which is bounded on $C_0^\infty(V)$ whenever $\overline{V}$ is compact, and which satisfies $l(L^*\varphi) = \langle f, \varphi \rangle$ for every $\varphi \in C_0^\infty$. Then $l$ is smooth in the sense that there exists $u \in C^\infty$ which represents $l$; that is, $l(t) = \langle u, t \rangle$ for every $t \in C_0^\infty$. Such a smooth representative $u$ of a weak solution $l$ is an actual solution, $Lu = f$.

15 Observe that the Cauchy-Riemann operator $(\partial/\partial x) + i(\partial/\partial y)$ is elliptic. Conclude from the general theory of elliptic operators that every holomorphic function is $C^{\infty}$. Prove that every holomorphic function is a complex-valued harmonic function on the plane, and use Green's 1st identity (Exercise 5, Chapter 4) to prove that a holomorphic function with compact support must be identically zero.

16 The Eigenvalues of the Laplacian This is an extended exercise in which the fundamental properties of the eigenfunctions and eigenvalues of the Laplacian are developed. Proofs for the more difficult parts are outlined, and in some cases are given nearly in full.

Consider the Laplace-Beltrami operator  $ \Delta $ acting on the p-forms  $ E^{p}(M) $ for some fixed p. A real number  $ \lambda $ corresponding to which there exists a not identically zero p-form u such that  $ \Delta u = \lambda u $ is called an eigenvalue of  $ \Delta $. If  $ \lambda $ is an eigenvalue, then any p-form u such that  $ \Delta u = \lambda u $ is called an eigenfunction of  $ \Delta $ corresponding to the eigenvalue  $ \lambda $. The eigenfunctions corresponding to a fixed  $ \lambda $ form a subspace of  $ E^{p}(M) $ called the eigenspace of the eigenvalue  $ \lambda $.

(a) Prove that the eigenvalues of  $ \Delta $ are non-negative.

(b) Prove that the eigenspaces of  $ \Delta $ are finite dimensional.

(c) Prove that the eigenvalues have no finite accumulation point.

(d) Prove that eigenfunctions corresponding to distinct eigenvalues are orthogonal.

(e) Existence. In order for the above statements to have substance we must prove that there exist eigenvalues of $\Delta$. First of all, zero is an eigenvalue if and only if there are non-trivial harmonic $p$-forms on $M$, and the corresponding eigenspace is precisely the space $H^p$ of harmonic forms. We shall now establish that $\Delta$ has a positive eigenvalue—in fact, a whole sequence of eigenvalues diverging to $+\infty$. Consider $\Delta$ to be restricted to $(H^p)^\perp$. Then we have $\Delta: (H^p)^\perp \to (H^p)^\perp$, and also we have the Green's operator $G: (H^p)^\perp \to (H^p)^\perp$, and $\Delta G\alpha = \alpha$, $G\Delta\alpha = \alpha$ for all $\alpha \in (H^p)^\perp$. Observe that the eigenvalues of $G \mid (H^p)^\perp$ are the reciprocals of the eigenvalues of $\Delta \mid (H^p)^\perp$. Let

 $$ \begin{array}{r}{\eta=\operatorname*{s u p}_{\|\varphi\|=1}\|G\varphi\|.}\\ {\varphi e(H^{p})^{\perp}}\end{array} $$ 

Then $\eta > 0$ and $\|G\varphi\| \leq \eta \|\varphi\|$ for every $\varphi \in (H^{\varphi})^{\perp}$. We shall prove that $1/\eta$ is an eigenvalue of $\Delta$. Let $\{\varphi_j\} \in (H^{\varphi})^{\perp}$ be a maximizing sequence for $\eta$; that is, $\|\varphi_j\| = 1$ and $\|G\varphi_j\| \to \eta$.

First, we claim that  $ \|G^2\varphi_j - \eta^2\varphi_j\| \to 0 $, for

 $$ \begin{aligned}{\|G^{\mathtt{s}}\varphi_{j}-\eta^{\mathtt{s}}\varphi_{j}\|^{\mathtt{s}}}&{{}=\|G^{\mathtt{s}}\varphi_{j}\|^{\mathtt{s}}-2\eta^{\mathtt{s}}\langle G^{\mathtt{s}}\varphi_{j},\varphi_{j}\rangle+\eta^{4}}\\ {}&{{}\leq\eta^{\mathtt{s}}\|G\varphi_{j}\|^{\mathtt{s}}\cdot-2\eta^{\mathtt{s}}\|G\varphi_{j}\|^{\mathtt{s}}+\eta^{4}\to0.}\\ \end{aligned} $$ 

Second, we claim that  $ \|G\varphi_j - \eta\varphi_j\| \to 0 $. For if we let  $ \psi_j = G\varphi_j - \eta\varphi_j $, then

where we have used the fact that  $ \langle\psi_i,G\psi_i\rangle\geq0 $. (Why?) Now there is a subsequence of the  $ \varphi_i $, call it  $ \{\varphi_i\} $, such that  $ \{G\varphi_i\} $ is Cauchy. Define a linear functional  $ I $ on  $ E^p(M) $ by setting

 $$ \begin{aligned}{0\leftarrow\langle\psi_{j},G^{2}\varphi_{j}-\eta^{3}\varphi_{j}\rangle}\\ {=\langle\psi_{j},G\psi_{j}+\eta\psi_{j}\rangle}\\ {=\langle\psi_{j},G\psi_{j}\rangle+\dot{\eta}\Vert\psi_{j}\Vert^{3}\geq\eta\Vert\psi_{j}\Vert^{3},}\\ \end{aligned} $$ 

 $$ \begin{array}{r}{I(\beta)=\operatorname*{l i m}_{j\to\infty}\eta\langle G\varphi_{j},\beta\rangle\quad\mathrm{f o r}\quad\beta\in E^{v}(M).}\end{array} $$ 

Prove that $l$ is a non-trivial weak solution of

 $$ \big(\Delta-(1/\eta)\big)u=0. $$ 

From this and the fact that  $ \Delta - 1/\eta $ is elliptic, conclude that  $ \lambda = 1/\eta $ is an eigenvalue of  $ \Delta $.

(f) Existence of Other Eigenvalues. Suppose that we have eigenvalues  $ \lambda_1 \leq \lambda_2 \leq \cdots \leq \lambda_n $ and corresponding eigenfunctions  $ u_1, u_2, \ldots, u_n $ (orthonormalized) for  $ \Delta \big| (H^p)^{\perp}  $. Let  $ R_n $ be the subspace of  $ (H^p)^{\perp} $ spanned by  $ \{u_1, \ldots, u_n\} $. Observe that  $ G $ and  $ \Delta $ map  $ (H^p \oplus R_n)^{\perp} $ into itself, then define

 $$ \eta_{n+1}=\operatorname*{s u p}_{\substack{\|\varphi\|-1\\ \varphi\in(H^{p}\oplus R_{n})^{\perp}}}\|G\varphi\| $$ 

and proceed as in part (e) to establish that  $ \lambda_{n+1} = 1/\eta_{n+1} $ is an eigenvalue of  $ \Delta $. Clearly,  $ \lambda_{n+1} \geq \lambda_n $.

(g) $L_{2}$ Completeness. Let $\lambda_{1} \leq \lambda_{2} \leq \cdots \leq$ be the eigenvalues of $\Delta$ on $E^{p}(M)$, where each eigenvalue is included as many times as the dimension of its eigenspace, with a corresponding orthonormalized sequence of eigenfunctions $\{u_{i}\}$. Let $\alpha \in E^{p}(M)$. Then

 $$ \lim_{n\to\infty}\left\|\alpha-\sum_{i=1}^{n}\langle\alpha,u_{i}\rangle u_{i}\right\|=0. $$ 

For the proof, let $k$ be the dimension of $H^p$. Then there exists $\beta \in (H^p)^\perp$ such that $G\beta = \alpha - \sum_{i=1}^{k} \langle \alpha, u_i \rangle u_i$. It follows that

 $$ \left\|\alpha-\sum_{i=1}^{n}\langle\alpha,u_{i}\rangle u_{i}\right\|=\left\|G\left(\beta-\sum_{i=k+1}^{n}\langle\beta,u_{i}\rangle u_{i}\right)\right\| $$ 

for $n > k$. But, by the definition of $\lambda_{n+1}$,

 $$ \begin{align*}\bigg\|G\bigg(\beta-\sum_{i=k+1}^{n}\langle\beta,u_{i}\rangle u_{i}\bigg)\bigg\|&\leq\frac{1}{\lambda_{n+1}}\bigg\|\beta-\sum_{i=k+1}^{n}\langle\beta,u_{i}\rangle u_{i}\bigg\|\\&\leq\frac{1}{\lambda_{n+1}}\|\beta\|\to0\quad as\quad n\to\infty.\end{align*} $$ 

(h) Uniform Completeness. The uniform norm  $ \|\alpha\|_{\infty} $ is defined on  $ E^{p}(M) $ by

 $$ \|\alpha\|_{\infty}=\operatorname*{s u p}_{m\in\mathcal{M}}\left(*(\alpha\land*\alpha)(m)\right)^{1/3}. $$ 

From the Sobolev inequality 6.22(1) and the compactness of $M$, one can conclude that there exists a large enough integer $k$ and a constant $c > 0$ such that

 $$ \|\alpha\|_{\infty}\leq c\|(1+\Delta)^{k}\alpha\| $$ 

for every $\alpha \in E^p(M)$. Let $\alpha \in E^p(M)$, and let $P_n(\alpha) = \sum_{i=1}^{n} \langle \alpha, u_i \rangle u_i$, where we are continuing with the notation of part (g). Now $\Delta P_n = P_n \Delta$, so that

 $$ \begin{aligned}{\|\alpha-P_{n}(\alpha)\|_{\infty}}&{{}\leq c\left\|(1+\Delta)^{k}[\alpha-P_{n}(\alpha)]\right\|}\\ {}&{{}=\|\varphi-P_{n}\varphi\|\to0,}\\ \end{aligned} $$ 

where  $ \varphi = (1 + \Delta)^{k}\alpha $.

17 We define the operator  $ \Delta^s \colon E^p(M) \to E^p(M) $ by  $ \Delta^s(\alpha) = \Delta(\Delta\alpha) $. Discuss the solvability of  $ \Delta^s\alpha = \beta $.

18 Consider the operator

 $$ L=\sum_{i,j=1}^{n}a_{ij}\frac{\partial^{2}}{\partial x_{i}\partial x_{j}}+\sum_{i=1}^{n}b_{i}\frac{\partial}{\partial x_{i}}+c $$ 

acting on $C^{2}(\mathbb{R}^{n})$. Show that there is no loss of generality in assuming that $a_{ij}=a_{ji}$, and prove that $L$ is elliptic at a point $x$ if and only if the matrix $(a_{ij}(x))$ is (positive or negative) definite. In particular, show that the wave equation

 $$ \Box u=\frac{\partial^{2}u}{\partial x^{2}}-\frac{\partial^{2}u}{\partial y^{2}}=f $$ 

is not elliptic, and give an example where

 $$ \Box u=f\in C^{\infty}\quad\mathrm{b u t}\quad u\notin C^{\infty}. $$ 

19 Consider $\Delta\colon E^p(M)\to E^p(M)$. Prove that if $\lambda$ is the minimum eigenvalue of $\Delta$, and if $c>-\lambda$, then $(\Delta+c)\alpha=\beta$ can be solved for every $\beta\in E^p(M)$.

20 The Peter-Weyl Theorem The representative ring of a compact Lie group $G$ is the ring generated over the complex numbers by the set of all continuous functions $f$ for which there is a continuous homomorphism $\rho: G \to G/(n, \mathbb{C})$ for some $n$ such that $f = \rho_{ij}$ for some choice of $i$ and $j$. The Peter-Weyl theorem states that the representative ring is dense in the space of complex-valued continuous functions on $G$ in the uniform norm. That is, if $g$ is a complex-valued continuous function on $G$, and if $\varepsilon > 0$ is given, then there is a function $f$ in the representative ring such that $|f(\sigma) - g(\sigma)| < \varepsilon$ for all $\sigma \in G$. We outline a proof of this theorem which is based on the uniform completeness of the eigenfunctions of the Laplacian. One can choose a Riemannian structure on $G$ such that each of the diffeomorphisms $l_\sigma$ for $\sigma \in G$ (left translation by $\sigma$) is an isometry (that is, $\langle v, w \rangle_\tau = \langle dl_\sigma v, dl_\sigma w \rangle_\sigma$ for all $\tau \in G$ and all $v, w \in G_\tau$). Since the $C^\infty$ functions are dense in the space of continuous functions in the uniform norm, and since by Exercise 16(h) the direct sum of the eigenspaces of the Laplacian is dense in the space of $C^\infty$ functions in the uniform norm, it suffices for the Peter-Weyl theorem to prove that each eigenfunction of the Laplacian $\Delta: C^\infty(G) \to C^\infty(G)$ belongs to the representative ring.

Now, G acts on the  $ C^{\infty} $ functions on G by

 $$ \sigma(f)=f\circ l_{*}\quad\mathrm{f o r~}\sigma\in G. $$ 

Prove that since the $l_{e}$ are isometries, this action commutes with the Laplacian:

 $$ \Delta(f\circ l_{e})=(\Delta f)\circ l_{e}\qquad(\sigma\in G). $$ 

Let $V_\lambda$ be the (finite dimensional) eigenspace associated with the eigenvalue $\lambda$ of $\Delta$: $C^\infty(G) \to C^\infty(G)$. Prove that the action of $G$ leaves $V_\lambda$ invariant. Then let $\varphi_1, \ldots, \varphi_n$ be a basis of $V_\lambda$, and let

 $$ \sigma(\varphi_{i})=\sum_{j}g_{i j}(\sigma)\varphi_{j}. $$ 

Then $\sigma \mapsto \{g_{if}(\sigma)\}$ is a homomorphism of $G \to Gl(n, \mathbb{R})$. Prove that this homomorphism is continuous. Then observe that

 $$ \varphi_{i}(\sigma)=\varphi_{i}\circ l_{\sigma}(e)=\sum_{j}g_{i j}(\sigma)\varphi_{j}(e), $$ 

so that  $ \varphi_{i} $ belongs to the representative ring.

21 The reader who is familiar with the theory of vector bundles should observe that the results in this chapter on the Laplace-Beltrami operator are valid for general elliptic operators on vector bundles. We outline the statements of the results in this situation:

Let $E$ and $F$ be (real or complex) vector bundles over a compact orientable manifold $M$. Let $C^\infty(E)$ and $C^\infty(F)$ denote the vector spaces of smooth sections of $E$ and $F$ respectively. A (linear) differential operator $L$ of order $l$ from $E$ to $F$ is a linear map from $C^\infty(E)$ to $C^\infty(F)$ which when expressed in terms of local trivialization of $E$ and $F$ yields an ordinary linear partial differential operator of order $l$. The operator $L$ is elliptic if it is locally elliptic. Equivalently, ellipticicity of $L$ can be defined in terms of the symbol as in 6.36. Observe that for $L$ to be elliptic, the fibre dimensions of $E$ and $F$ must be equal. Choose inner products in the fibres $E_m$ and $F_m$ which vary smoothly with $m$, and choose a Riemannian structure and an orientation on $M$ with respect to which smooth functions can be integrated over $M$. By integrating the fibre inner products over $M$, we obtain inner products on $C^\infty(E)$ and $C^\infty(F)$. Let $L: C^\infty(E) \to C^\infty(F)$ be a differential operator. Prove that $L$ has a formal adjoint $L^*: C^\infty(F) \to C^\infty(E)$. Assume that $L$ is elliptic.

(a) Prove that ker L and ker  $ L^{*} $ are finite dimensional.

(b) Prove that  $ C^{\infty}(E) $ and  $ C^{\infty}(F) $ have the following orthogonal direct sum decompositions:

 $$ \begin{aligned}{}&{{}C^{\infty}(F)=L\big(C^{\infty}(E)\big)\oplus\ker L^{*},}\\ {}&{{}C^{\infty}(E)=L^{*}\big(C^{\infty}(F)\big)\oplus\ker L.}\\ \end{aligned} $$ 

22 Let $\varphi_n$, for $n=1,2,3,\ldots$, be a periodic $C^\infty$ function on the plane which agrees with $\log \log(1/(r+(1/n)))$ for $0 \leq r \leq \frac{1}{2}$, where $r = \sqrt{x^2 + y^2}$. Show that there is no constant $c > 0$ such that

 $$ \left\|\varphi_{n}\right\|_{\infty}\leq c\left\|\varphi_{n}\right\|_{1}\qquad\mathrm{f o r~a l l~}n. $$ 

This shows, in the case $n=2$, that the restriction $t\geq[n/2]+1$ in Corollary (b) of the Sobolev lemma 6.22 is essential.

23 Let $L$ be a (linear) elliptic operator on the $C^\infty$ functions on a compact oriented Riemannian manifold $M$. Let $\gamma$ be a diffeomorphism of $M$ which preserves the volume form on $M$. We say that a $C^\infty$ function $f$ on $M$ is invariant under $\gamma$ if $f\circ\gamma=f$, and we say that the operator $L$ is invariant under $\gamma$ if $Lu\circ\gamma=L(u\circ\gamma)$ for all $C^\infty$ functions $u$ on $M$. Suppose that $L$ and $f$ are invariant under $\gamma$ and that $f$ is orthogonal to the kernel of $L^*$. Prove that there is an invariant solution $u$ of $Lu=f$.
