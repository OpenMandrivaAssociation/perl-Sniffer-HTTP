%define upstream_name	  Sniffer-HTTP
%define upstream_version  0.22


Name:		perl-%{upstream_name}
Summary:	Multi-connection sniffer driver
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1
URL:		http://search.cpan.org/~corion/Sniffer-HTTP-0.22/lib/Sniffer/HTTP.pm
Source0:	http://search.cpan.org/CPAN/authors/id/C/CO/CORION/%{upstream_name}-%{upstream_version}.tar.gz	
License:	Artistic
Group:		Development/Perl 
BuildRequires:	perl(NetPacket)
BuildRequires:	perl(Net::Pcap)
BuildRequires:	perl(Exporter::Lite)
BuildRequires:	perl(LWP::Simple)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Class::Accessor)
Buildarch:	noarch

%description
This driver gives you callbacks with the completely accumulated HTTP::Requests or HTTP::Responses as sniffed from the TCP traffic. You need to feed it the Ethernet, IP or TCP packets either from a dump file or from Net::Pcap by unpacking them via NetPacket.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes MANIFEST META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
