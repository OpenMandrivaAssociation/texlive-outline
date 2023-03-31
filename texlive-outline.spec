Name:		texlive-outline
Version:	18360
Release:	2
Summary:	List environment for making outlines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/outline
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/outline.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/outline.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
