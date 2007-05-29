#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Verilog
%define	pnam	Perl
Summary:	Verilog::Perl - an Perl way to handle Verilog files
Summary(pl.UTF-8):	Verilog::Perl - perlowy sposób obsługi plików Verilog
Name:		perl-Verilog-Perl
Version:	2.380
Release:	1
License:	LGPL or Perl Artistic License
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	536d4e72be7e96b5cc81fe5e9dc90ecb
URL:		http://search.cpan.org/dist/Verilog-Perl/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Verilog::Parser, Verilog::Preproc, and other Perl modules useful for
manipulation of Verilog files. The Verilog::Parser package will
tokenize a Verilog file when the parse() method is called and invoke
various callback methods. This is useful for extracting information
and editing files while retaining all context. For netlist like
extractions, see Verilog::Netlist. Verilog::Preproc reads Verilog
files, and preprocesses them according to the Verilog 2001
specification. Programs can be easily converted from reading a
IO::File into reading preprocessed output from Verilog::Preproc.
Verilog::Netlist contains interconnect information about a whole
design database.

%description -l pl.UTF-8
Verilog::Parser, Verilog::Preproc i inne moduły Perla przydatne do
obróbki plików Verilog. Pakiet Verilog::Parser po wywołaniu metody
parse() zamienia plik Verilog na tokeny i wykonuje różne metody
wywołań zwrotnych. Jest to przydatne przy wyciąganiu informacji i
modyfikowaniu plików z zachowaniem całego kontekstu. Do wyciągania
informacji w stylu netlist można użyć Verilog::Netlist.
Verilog::Preproc czyta pliki Verilog i przetwarza je zgodnie ze
specyfikacją Verilog 2001. Można łatwo przekształcać programy z
odczytu za pomocą IO::File na czytanie przetworzonego wyjścia z
Verilog::Preproc. Verilog::Netlist zawiera dołączone informacje o
całej bazie projektu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

# maybe bin/man1 should be moved to another package
%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorarch}/Verilog
%{perl_vendorarch}/Verilog/*.pm
%dir %{perl_vendorarch}/Verilog/Netlist
%{perl_vendorarch}/Verilog/Netlist/*.pm
%dir %{perl_vendorarch}/auto/Verilog/Preproc
%{perl_vendorarch}/auto/Verilog/Preproc/Preproc.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Verilog/Preproc/Preproc.so
%{_mandir}/man1/*
%{_mandir}/man3/*
