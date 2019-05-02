# revision 18360
# category Package
# catalog-ctan /macros/latex/contrib/outline
# catalog-date 2010-05-19 18:21:51 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-outline
Version:	20190228
Release:	1
Summary:	List environment for making outlines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/outline
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/outline.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/outline.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines an outline environment, which provides
facilities similar to enumerate, but up to 6 levels deep.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/outline/outline.sty
%doc %{_texmfdistdir}/doc/latex/outline/README
%doc %{_texmfdistdir}/doc/latex/outline/outline-sample.tex
%doc %{_texmfdistdir}/doc/latex/outline/outline.pdf
%doc %{_texmfdistdir}/doc/latex/outline/outline.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100519-2
+ Revision: 754561
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100519-1
+ Revision: 719174
- texlive-outline
- texlive-outline
- texlive-outline
- texlive-outline

