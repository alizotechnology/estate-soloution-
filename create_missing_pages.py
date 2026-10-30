import os
import sys

sys.path.append('/home/jules/self_created_tools')
from build_portal import generate_header, generate_footer, generate_widgets, LOGO_ANIMATION_CSS

def build_about():
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About Us | Estate Solutions - DHA Bahawalpur Advisory</title>
  <meta name="description" content="Learn about Estate Solutions and Rasheed Baig, leading real estate consultants in DHA Bahawalpur specializing in Takmeel Square, Pelican Mall, and Defence Gardenia Villas.">
  <script src="https://cdn.tailwindcss.com"></script>
  <script id="tailwind-config">
    tailwind.config = {{
      darkMode: "class",
      theme: {{
        extend: {{
          colors: {{
            "surface": "#f8f9fa",
            "on-surface": "#191c1d",
            "on-surface-variant": "#45464c",
            "slate-black": "#0B0F17",
            "dark-surface": "#161F30",
            "dark-border": "#283548",
            "luxe-gold-light": "#DFBA73",
            "luxe-gold-deep": "#9E7B35",
            "secondary": "#775a19",
            "ivory-base": "#FCFCFD",
            "charcoal-border": "#E5E7EB"
          }},
          fontFamily: {{
            "display-xl": ["Playfair Display", "serif"],
            "headline-lg": ["Playfair Display", "serif"],
            "body-md": ["Plus Jakarta Sans", "sans-serif"],
            "label-lg": ["Plus Jakarta Sans", "sans-serif"]
          }}
        }}
      }}
    }};
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  {LOGO_ANIMATION_CSS}
</head>
<body class="bg-surface font-body-md text-on-surface antialiased flex flex-col min-h-screen">
  {generate_header("about")}

  <main class="flex-grow pt-24">
    <!-- Hero Banner -->
    <section class="bg-slate-black text-ivory-base py-16 md:py-24 border-b border-dark-border relative overflow-hidden">
      <div class="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-dark-surface border border-luxe-gold-light/30 text-luxe-gold-light text-xs uppercase tracking-widest mb-4">
          <i class="fa-solid fa-award"></i> Executive Heritage & Advisory
        </div>
        <h1 class="font-display-xl text-3xl sm:text-5xl font-bold tracking-tight mb-4 text-white">
          Architecting Wealth & Investment Security in <span class="italic text-luxe-gold-light">DHA Bahawalpur</span>
        </h1>
        <p class="text-outline-variant text-base sm:text-lg max-w-3xl leading-relaxed">
          Under the executive leadership of Rasheed Baig, Estate Solutions stands as the premier institutional real estate advisory for discernment-driven investors, local buyers, and overseas Pakistani diaspora.
        </p>
      </div>
    </section>

    <!-- Executive Leadership Section -->
    <section class="py-16 max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-5 relative">
          <div class="relative rounded-2xl overflow-hidden border border-charcoal-border shadow-2xl bg-slate-black p-3">
            <img src="/assets/images/logo.jpg" alt="Estate Solutions Brand Emblem" class="w-full h-auto rounded-xl object-cover animated-logo">
            <div class="p-6 bg-dark-surface text-ivory-base rounded-xl mt-3 border border-dark-border">
              <span class="text-xs uppercase text-luxe-gold-light tracking-widest font-semibold block mb-1">Founder & Managing Lead</span>
              <h3 class="font-display-xl text-2xl font-bold">Rasheed Baig</h3>
              <p class="text-xs text-outline-variant mt-2 leading-relaxed">
                Over 15+ years of institutional real estate expertise, specializing in DHA Bahawalpur commercial sectors, residential plot files, possession-ready villas, and high-yield retail spaces.
              </p>
              <div class="mt-4 pt-4 border-t border-dark-border flex items-center justify-between">
                <a href="tel:03458530848" class="text-xs text-luxe-gold-light font-bold hover:underline"><i class="fa-solid fa-phone mr-1"></i> 0345-8530848</a>
                <a href="tel:03053001401" class="text-xs text-luxe-gold-light font-bold hover:underline"><i class="fa-solid fa-phone mr-1"></i> 0305-3001401</a>
              </div>
            </div>
          </div>
        </div>

        <div class="lg:col-span-7 flex flex-col gap-6">
          <span class="text-xs font-bold uppercase tracking-widest text-secondary">Our Pillar Values</span>
          <h2 class="font-display-xl text-3xl font-bold text-on-surface">Uncompromising Integrity, Verified Due Diligence & Market Intelligence</h2>
          <p class="text-on-surface-variant leading-relaxed">
            At Estate Solutions, we reject standard transactional sales pitches in favor of rigorous, institutional-grade due diligence. Every plot file, commercial space, or residential villa represented by our consultancy is thoroughly audited against DHA Bahawalpur masterplan records, title deeds, transfer history, and possession readiness.
          </p>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 pt-4">
            <div class="p-5 bg-white rounded-xl border border-charcoal-border shadow-sm">
              <div class="w-10 h-10 rounded-lg bg-surface-container-low flex items-center justify-center text-secondary mb-3">
                <i class="fa-solid fa-file-circle-check text-xl"></i>
              </div>
              <h4 class="font-bold text-base mb-1">DHA Title Verification</h4>
              <p class="text-xs text-on-surface-variant leading-relaxed">Guaranteed legal record checking at DHA Bahawalpur transfer offices before any transaction takes place.</p>
            </div>

            <div class="p-5 bg-white rounded-xl border border-charcoal-border shadow-sm">
              <div class="w-10 h-10 rounded-lg bg-surface-container-low flex items-center justify-center text-secondary mb-3">
                <i class="fa-solid fa-globe text-xl"></i>
              </div>
              <h4 class="font-bold text-base mb-1">Overseas Client Desk</h4>
              <p class="text-xs text-on-surface-variant leading-relaxed">Seamless power-of-attorney execution, video verification, and transparent wire transfer processing for diaspora buyers.</p>
            </div>

            <div class="p-5 bg-white rounded-xl border border-charcoal-border shadow-sm">
              <div class="w-10 h-10 rounded-lg bg-surface-container-low flex items-center justify-center text-secondary mb-3">
                <i class="fa-solid fa-chart-line text-xl"></i>
              </div>
              <h4 class="font-bold text-base mb-1">High ROI Analytics</h4>
              <p class="text-xs text-on-surface-variant leading-relaxed">Strategic allocation in high-growth corridors like Takmeel Square, Pelican Mall, and Sector A 1-Kanal avenues.</p>
            </div>

            <div class="p-5 bg-white rounded-xl border border-charcoal-border shadow-sm">
              <div class="w-10 h-10 rounded-lg bg-surface-container-low flex items-center justify-center text-secondary mb-3">
                <i class="fa-solid fa-handshake-simple text-xl"></i>
              </div>
              <h4 class="font-bold text-base mb-1">Direct Seller & Developer Access</h4>
              <p class="text-xs text-on-surface-variant leading-relaxed">Direct negotiation with certified owners and authorized master developers without artificial markups.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Key Statistics -->
    <section class="bg-slate-black text-ivory-base py-16 border-y border-dark-border">
      <div class="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
          <div>
            <span class="font-display-xl text-4xl sm:text-5xl font-bold text-luxe-gold-light block">15+</span>
            <span class="text-xs uppercase tracking-widest text-outline-variant mt-2 block">Years Industry Authority</span>
          </div>
          <div>
            <span class="font-display-xl text-4xl sm:text-5xl font-bold text-luxe-gold-light block">500+</span>
            <span class="text-xs uppercase tracking-widest text-outline-variant mt-2 block">Verified DHA Transactions</span>
          </div>
          <div>
            <span class="font-display-xl text-4xl sm:text-5xl font-bold text-luxe-gold-light block">100%</span>
            <span class="text-xs uppercase tracking-widest text-outline-variant mt-2 block">Document Legal Assurance</span>
          </div>
          <div>
            <span class="font-display-xl text-4xl sm:text-5xl font-bold text-luxe-gold-light block"> PKR 3B+</span>
            <span class="text-xs uppercase tracking-widest text-outline-variant mt-2 block">Assets Managed & Portfolio</span>
          </div>
        </div>
      </div>
    </section>
  </main>

  {generate_footer()}
  {generate_widgets()}
</body>
</html>
"""
    os.makedirs('about', exist_ok=True)
    with open('about/index.html', 'w') as f:
        f.write(content)
    print("Created about/index.html")

def build_services():
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Services | Estate Solutions - DHA Bahawalpur Real Estate Services</title>
  <meta name="description" content="Explore our bespoke real estate advisory, plot acquisition, commercial leasing, and overseas investment desk services in DHA Bahawalpur.">
  <script src="https://cdn.tailwindcss.com"></script>
  <script id="tailwind-config">
    tailwind.config = {{
      darkMode: "class",
      theme: {{
        extend: {{
          colors: {{
            "surface": "#f8f9fa",
            "on-surface": "#191c1d",
            "on-surface-variant": "#45464c",
            "slate-black": "#0B0F17",
            "dark-surface": "#161F30",
            "dark-border": "#283548",
            "luxe-gold-light": "#DFBA73",
            "luxe-gold-deep": "#9E7B35",
            "secondary": "#775a19",
            "ivory-base": "#FCFCFD",
            "charcoal-border": "#E5E7EB"
          }},
          fontFamily: {{
            "display-xl": ["Playfair Display", "serif"],
            "headline-lg": ["Playfair Display", "serif"],
            "body-md": ["Plus Jakarta Sans", "sans-serif"]
          }}
        }}
      }}
    }};
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  {LOGO_ANIMATION_CSS}
</head>
<body class="bg-surface font-body-md text-on-surface antialiased flex flex-col min-h-screen">
  {generate_header("services")}

  <main class="flex-grow pt-24">
    <!-- Hero Banner -->
    <section class="bg-slate-black text-ivory-base py-16 md:py-24 border-b border-dark-border relative overflow-hidden">
      <div class="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-dark-surface border border-luxe-gold-light/30 text-luxe-gold-light text-xs uppercase tracking-widest mb-4">
          <i class="fa-solid fa-list-check"></i> Institutional Advisory Services
        </div>
        <h1 class="font-display-xl text-3xl sm:text-5xl font-bold tracking-tight mb-4 text-white">
          Comprehensive Real Estate <span class="italic text-luxe-gold-light">Solutions & Advisory</span>
        </h1>
        <p class="text-outline-variant text-base sm:text-lg max-w-3xl leading-relaxed">
          From verified plot file transfers to turnkey luxury villa acquisition and high-yield commercial space leasing in DHA Bahawalpur.
        </p>
      </div>
    </section>

    <!-- Services Grid -->
    <section class="py-16 max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Service 1 -->
        <div class="bg-white rounded-2xl p-8 border border-charcoal-border shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-slate-black text-luxe-gold-light flex items-center justify-center text-2xl mb-6 shadow-md">
              <i class="fa-solid fa-landmark"></i>
            </div>
            <h3 class="font-display-xl text-xl font-bold text-on-surface mb-3">Residential Plot Acquisition</h3>
            <p class="text-sm text-on-surface-variant leading-relaxed">
              Curated selection of 5 Marla, 10 Marla, 1 Kanal, and 2 Kanal prime residential plots across Sector A, B, C, N, and Villa Enclave in DHA Bahawalpur. Complete file verification included.
            </p>
          </div>
          <div class="pt-6 mt-6 border-t border-charcoal-border/50">
            <a href="/buy-sell" class="text-xs uppercase tracking-wider font-bold text-secondary hover:text-black flex items-center justify-between">
              Browse Plot Listings <i class="fa-solid fa-arrow-right"></i>
            </a>
          </div>
        </div>

        <!-- Service 2 -->
        <div class="bg-white rounded-2xl p-8 border border-charcoal-border shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-slate-black text-luxe-gold-light flex items-center justify-center text-2xl mb-6 shadow-md">
              <i class="fa-solid fa-building-user"></i>
            </div>
            <h3 class="font-display-xl text-xl font-bold text-on-surface mb-3">Commercial Retail & Offsite Leasing</h3>
            <p class="text-sm text-on-surface-variant leading-relaxed">
              High-footfall retail units, corporate offices, and restaurant venues at Takmeel Square and Pelican Mall Swiss International. Ideal for capital growth and steady rental yield.
            </p>
          </div>
          <div class="pt-6 mt-6 border-t border-charcoal-border/50">
            <a href="/takmeel-square" class="text-xs uppercase tracking-wider font-bold text-secondary hover:text-black flex items-center justify-between">
              Explore Commercial Assets <i class="fa-solid fa-arrow-right"></i>
            </a>
          </div>
        </div>

        <!-- Service 3 -->
        <div class="bg-white rounded-2xl p-8 border border-charcoal-border shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-slate-black text-luxe-gold-light flex items-center justify-center text-2xl mb-6 shadow-md">
              <i class="fa-solid fa-house-lock"></i>
            </div>
            <h3 class="font-display-xl text-xl font-bold text-on-surface mb-3">Defence Gardenia Luxury Villas</h3>
            <p class="text-sm text-on-surface-variant leading-relaxed">
              Turnkey 6 Marla and 10 Marla luxury villas with flexible 3-year installment plans. Modern architectural elevations, smart home automation options, and possession guarantees.
            </p>
          </div>
          <div class="pt-6 mt-6 border-t border-charcoal-border/50">
            <a href="/defence-gardenia-villas" class="text-xs uppercase tracking-wider font-bold text-secondary hover:text-black flex items-center justify-between">
              View Villa Layouts <i class="fa-solid fa-arrow-right"></i>
            </a>
          </div>
        </div>

        <!-- Service 4 -->
        <div class="bg-white rounded-2xl p-8 border border-charcoal-border shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-slate-black text-luxe-gold-light flex items-center justify-center text-2xl mb-6 shadow-md">
              <i class="fa-solid fa-file-shield"></i>
            </div>
            <h3 class="font-display-xl text-xl font-bold text-on-surface mb-3">DHA Legal & Title Due Diligence</h3>
            <p class="text-sm text-on-surface-variant leading-relaxed">
              Comprehensive verification of allotment letters, NDC (No Demand Certificate), encumbrance checks, and transfer tax calculations at the official DHA Bahawalpur transfer counter.
            </p>
          </div>
          <div class="pt-6 mt-6 border-t border-charcoal-border/50">
            <a href="/contact" class="text-xs uppercase tracking-wider font-bold text-secondary hover:text-black flex items-center justify-between">
              Request Verification <i class="fa-solid fa-arrow-right"></i>
            </a>
          </div>
        </div>

        <!-- Service 5 -->
        <div class="bg-white rounded-2xl p-8 border border-charcoal-border shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-slate-black text-luxe-gold-light flex items-center justify-center text-2xl mb-6 shadow-md">
              <i class="fa-solid fa-plane-arrival"></i>
            </div>
            <h3 class="font-display-xl text-xl font-bold text-on-surface mb-3">Overseas Investor Concierge Desk</h3>
            <p class="text-sm text-on-surface-variant leading-relaxed">
              Dedicated liaison service for Pakistani expats in UK, UAE, USA, Europe, and GCC. Includes remote video walkthroughs, digital documentation, and Power of Attorney handling.
            </p>
          </div>
          <div class="pt-6 mt-6 border-t border-charcoal-border/50">
            <a href="/contact" class="text-xs uppercase tracking-wider font-bold text-secondary hover:text-black flex items-center justify-between">
              Book VIP Overseas Call <i class="fa-solid fa-arrow-right"></i>
            </a>
          </div>
        </div>

        <!-- Service 6 -->
        <div class="bg-white rounded-2xl p-8 border border-charcoal-border shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-slate-black text-luxe-gold-light flex items-center justify-center text-2xl mb-6 shadow-md">
              <i class="fa-solid fa-calculator"></i>
            </div>
            <h3 class="font-display-xl text-xl font-bold text-on-surface mb-3">Property Valuation & Selling Assistance</h3>
            <p class="text-sm text-on-surface-variant leading-relaxed">
              Real-time market valuation for plot owners looking to liquidate or upgrade assets. Targeted buyer matching and marketing campaigns for fast, transparent transfers.
            </p>
          </div>
          <div class="pt-6 mt-6 border-t border-charcoal-border/50">
            <a href="/buy-sell" class="text-xs uppercase tracking-wider font-bold text-secondary hover:text-black flex items-center justify-between">
              Submit Your Property <i class="fa-solid fa-arrow-right"></i>
            </a>
          </div>
        </div>
      </div>
    </section>
  </main>

  {generate_footer()}
  {generate_widgets()}
</body>
</html>
"""
    os.makedirs('services', exist_ok=True)
    with open('services/index.html', 'w') as f:
        f.write(content)
    print("Created services/index.html")

def build_faq():
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Investor FAQ | Estate Solutions - DHA Bahawalpur</title>
  <meta name="description" content="Frequently Asked Questions regarding DHA Bahawalpur property transfers, plot prices, Takmeel Square, Pelican Mall, and overseas buyer procedures.">
  <script src="https://cdn.tailwindcss.com"></script>
  <script id="tailwind-config">
    tailwind.config = {{
      darkMode: "class",
      theme: {{
        extend: {{
          colors: {{
            "surface": "#f8f9fa",
            "on-surface": "#191c1d",
            "on-surface-variant": "#45464c",
            "slate-black": "#0B0F17",
            "dark-surface": "#161F30",
            "dark-border": "#283548",
            "luxe-gold-light": "#DFBA73",
            "secondary": "#775a19",
            "ivory-base": "#FCFCFD",
            "charcoal-border": "#E5E7EB"
          }},
          fontFamily: {{
            "display-xl": ["Playfair Display", "serif"],
            "body-md": ["Plus Jakarta Sans", "sans-serif"]
          }}
        }}
      }}
    }};
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  {LOGO_ANIMATION_CSS}
</head>
<body class="bg-surface font-body-md text-on-surface antialiased flex flex-col min-h-screen">
  {generate_header("faq")}

  <main class="flex-grow pt-24">
    <!-- Hero Banner -->
    <section class="bg-slate-black text-ivory-base py-16 md:py-24 border-b border-dark-border relative overflow-hidden">
      <div class="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-dark-surface border border-luxe-gold-light/30 text-luxe-gold-light text-xs uppercase tracking-widest mb-4">
          <i class="fa-solid fa-circle-question"></i> Knowledgebase & Help
        </div>
        <h1 class="font-display-xl text-3xl sm:text-5xl font-bold tracking-tight mb-4 text-white">
          Frequently Asked <span class="italic text-luxe-gold-light">Investor Questions</span>
        </h1>
        <p class="text-outline-variant text-base sm:text-lg max-w-3xl leading-relaxed">
          Clear, authoritative answers to essential queries about buying, selling, transferring, and managing properties in DHA Bahawalpur.
        </p>
      </div>
    </section>

    <!-- FAQ Accordion List -->
    <section class="py-16 max-w-[1000px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col gap-4">
        <!-- Q1 -->
        <details class="bg-white border border-charcoal-border rounded-xl p-6 shadow-sm group [&_summary::-webkit-details-marker]:hidden" open>
          <summary class="flex items-center justify-between font-display-xl text-lg font-bold text-on-surface cursor-pointer select-none">
            <span>1. What is the official process for transferring a plot in DHA Bahawalpur?</span>
            <span class="w-8 h-8 rounded-full bg-surface-container-low flex items-center justify-center text-secondary group-open:rotate-180 transition-transform">
              <i class="fa-solid fa-chevron-down text-xs"></i>
            </span>
          </summary>
          <div class="mt-4 pt-4 border-t border-charcoal-border/50 text-sm text-on-surface-variant leading-relaxed space-y-2">
            <p>The transfer process in DHA Bahawalpur requires:</p>
            <ul class="list-disc pl-5 space-y-1">
              <li>Applying for NDC (No Demand Certificate) from DHA Bahawalpur.</li>
              <li>Verification of original allotment/allocation letter and membership.</li>
              <li>Payment of DHA transfer fees, stamp duty, and government taxes.</li>
              <li>Personal appearance at the DHA Bahawalpur transfer branch or execution via verified Power of Attorney for overseas clients.</li>
            </ul>
          </div>
        </details>

        <!-- Q2 -->
        <details class="bg-white border border-charcoal-border rounded-xl p-6 shadow-sm group [&_summary::-webkit-details-marker]:hidden">
          <summary class="flex items-center justify-between font-display-xl text-lg font-bold text-on-surface cursor-pointer select-none">
            <span>2. How can Overseas Pakistanis buy property without traveling to Pakistan?</span>
            <span class="w-8 h-8 rounded-full bg-surface-container-low flex items-center justify-center text-secondary group-open:rotate-180 transition-transform">
              <i class="fa-solid fa-chevron-down text-xs"></i>
            </span>
          </summary>
          <div class="mt-4 pt-4 border-t border-charcoal-border/50 text-sm text-on-surface-variant leading-relaxed">
            <p>Overseas clients can appoint an authorized representative through a Power of Attorney (POA) attested by the Pakistan Embassy/High Commission in their country of residence. Estate Solutions manages the complete paperwork and provides live video walkthroughs and document dispatch.</p>
          </div>
        </details>

        <!-- Q3 -->
        <details class="bg-white border border-charcoal-border rounded-xl p-6 shadow-sm group [&_summary::-webkit-details-marker]:hidden">
          <summary class="flex items-center justify-between font-display-xl text-lg font-bold text-on-surface cursor-pointer select-none">
            <span>3. What commercial opportunities are available at Takmeel Square?</span>
            <span class="w-8 h-8 rounded-full bg-surface-container-low flex items-center justify-center text-secondary group-open:rotate-180 transition-transform">
              <i class="fa-solid fa-chevron-down text-xs"></i>
            </span>
          </summary>
          <div class="mt-4 pt-4 border-t border-charcoal-border/50 text-sm text-on-surface-variant leading-relaxed">
            <p>Takmeel Square features premier commercial plots, retail shop spaces, and corporate offices with high expected footfall. Flexible installment plans starting with 25% down payment make it an exceptional choice for both rental income and capital gains.</p>
          </div>
        </details>

        <!-- Q4 -->
        <details class="bg-white border border-charcoal-border rounded-xl p-6 shadow-sm group [&_summary::-webkit-details-marker]:hidden">
          <summary class="flex items-center justify-between font-display-xl text-lg font-bold text-on-surface cursor-pointer select-none">
            <span>4. Are Defence Gardenia Villas possession-ready?</span>
            <span class="w-8 h-8 rounded-full bg-surface-container-low flex items-center justify-center text-secondary group-open:rotate-180 transition-transform">
              <i class="fa-solid fa-chevron-down text-xs"></i>
            </span>
          </summary>
          <div class="mt-4 pt-4 border-t border-charcoal-border/50 text-sm text-on-surface-variant leading-relaxed">
            <p>Yes, select units in Defence Gardenia Villas are possession-ready while others are under active construction on structured 3-year installment plans. All villas come with guaranteed DHA utility connections and modern elevation finishes.</p>
          </div>
        </details>

        <!-- Q5 -->
        <details class="bg-white border border-charcoal-border rounded-xl p-6 shadow-sm group [&_summary::-webkit-details-marker]:hidden">
          <summary class="flex items-center justify-between font-display-xl text-lg font-bold text-on-surface cursor-pointer select-none">
            <span>5. How do I contact Rasheed Baig directly for urgent consulting?</span>
            <span class="w-8 h-8 rounded-full bg-surface-container-low flex items-center justify-center text-secondary group-open:rotate-180 transition-transform">
              <i class="fa-solid fa-chevron-down text-xs"></i>
            </span>
          </summary>
          <div class="mt-4 pt-4 border-t border-charcoal-border/50 text-sm text-on-surface-variant leading-relaxed">
            <p>You can call directly on <strong>0345-8530848</strong> or <strong>0305-3001401</strong>, or use our floating WhatsApp button for an immediate personal response.</p>
          </div>
        </details>
      </div>
    </section>
  </main>

  {generate_footer()}
  {generate_widgets()}
</body>
</html>
"""
    os.makedirs('faq', exist_ok=True)
    with open('faq/index.html', 'w') as f:
        f.write(content)
    print("Created faq/index.html")

def build_terms():
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Terms of Service & DHA Protocol | Estate Solutions</title>
  <meta name="description" content="Terms of Service, legal disclaimers, and DHA Bahawalpur verification compliance standards for Estate Solutions.">
  <script src="https://cdn.tailwindcss.com"></script>
  <script id="tailwind-config">
    tailwind.config = {{
      darkMode: "class",
      theme: {{
        extend: {{
          colors: {{
            "surface": "#f8f9fa",
            "on-surface": "#191c1d",
            "on-surface-variant": "#45464c",
            "slate-black": "#0B0F17",
            "dark-surface": "#161F30",
            "dark-border": "#283548",
            "luxe-gold-light": "#DFBA73",
            "secondary": "#775a19",
            "ivory-base": "#FCFCFD",
            "charcoal-border": "#E5E7EB"
          }},
          fontFamily: {{
            "display-xl": ["Playfair Display", "serif"],
            "body-md": ["Plus Jakarta Sans", "sans-serif"]
          }}
        }}
      }}
    }};
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  {LOGO_ANIMATION_CSS}
</head>
<body class="bg-surface font-body-md text-on-surface antialiased flex flex-col min-h-screen">
  {generate_header("terms")}

  <main class="flex-grow pt-24">
    <!-- Hero Banner -->
    <section class="bg-slate-black text-ivory-base py-16 md:py-24 border-b border-dark-border relative overflow-hidden">
      <div class="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-dark-surface border border-luxe-gold-light/30 text-luxe-gold-light text-xs uppercase tracking-widest mb-4">
          <i class="fa-solid fa-scale-balanced"></i> Legal Protocol & Standard Operating Procedures
        </div>
        <h1 class="font-display-xl text-3xl sm:text-5xl font-bold tracking-tight mb-4 text-white">
          Terms of Service & <span class="italic text-luxe-gold-light">DHA Compliance</span>
        </h1>
        <p class="text-outline-variant text-base sm:text-lg max-w-3xl leading-relaxed">
          Operational terms, listing disclaimers, and statutory real estate guidelines governing client engagements at Estate Solutions.
        </p>
      </div>
    </section>

    <!-- Terms Content -->
    <section class="py-16 max-w-[1000px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-white rounded-2xl p-8 border border-charcoal-border shadow-sm space-y-8 text-on-surface-variant leading-relaxed">
        <div>
          <h2 class="font-display-xl text-2xl font-bold text-on-surface mb-3">1. Scope of Advisory Services</h2>
          <p class="text-sm">
            Estate Solutions acts as an authorized real estate consultancy for properties within Defence Housing Authority (DHA) Bahawalpur, Takmeel Square, Pelican Mall, and Defence Gardenia Villas. Information provided on this platform is curated directly from verified developers and DHA records.
          </p>
        </div>

        <div>
          <h2 class="font-display-xl text-2xl font-bold text-on-surface mb-3">2. Title & Document Verification Protocol</h2>
          <p class="text-sm">
            All plot file prices, inventory statuses, and dimensional blueprints are subjected to DHA transfer counter verification prior to agreement sign-off. Buyers and sellers are required to provide official CNIC/NICOP identification for NDC processing.
          </p>
        </div>

        <div>
          <h2 class="font-display-xl text-2xl font-bold text-on-surface mb-3">3. Overseas Transactions & Representation</h2>
          <p class="text-sm">
            Power of Attorney documentation executed outside Pakistan must adhere strictly to Ministry of Foreign Affairs (MOFA) and Pakistan High Commission attestation protocols before DHA property transfers can be finalized.
          </p>
        </div>

        <div>
          <h2 class="font-display-xl text-2xl font-bold text-on-surface mb-3">4. Disclaimer of Price Fluctuations</h2>
          <p class="text-sm">
            Market rates for DHA plot files and commercial units fluctuate in response to market dynamics. Official quotes provided by Rasheed Baig remain binding for the duration specified in written purchase offers.
          </p>
        </div>
      </div>
    </section>
  </main>

  {generate_footer()}
  {generate_widgets()}
</body>
</html>
"""
    os.makedirs('terms', exist_ok=True)
    with open('terms/index.html', 'w') as f:
        f.write(content)
    print("Created terms/index.html")

if __name__ == "__main__":
    build_about()
    build_services()
    build_faq()
    build_terms()
